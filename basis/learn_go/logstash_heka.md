## 1 Logstash ##
logstash 是开箱即用的日志搜集处理软件，可以把分散、多样化的日志搜集起来，进行自定义的处理，然后传输到指定位置，如某个服务器或文件。
#### 1.1 下载、安装、使用 ####
点击：[下载地址](https://www.elastic.co/downloads/logstash "下载地址")，选择对应的系统版本，然后：

**unzip logstash**
```
tar zxvf logstash-6.3.2.tar.gz
cd logstash-6.3.2
```
**prepare a config file**
```
# vi logstash.conf

input {
    stdin {}
}

output {
    stdout {
        codec => rubydebug
    }
}
```
**run**
```
# bin/logstash -f logstash.conf (or) logstash -e ""
# hello, world

{
       "message" => "hello, world",
      "@version" => "1",
    "@timestamp" => "2018-07-30T11:11:48.246Z",
          "host" => "localhost.localdomain"
}
```
#### 1.2 配置文件 ####
logstash 的核心功能就体现在配置文件的 `input/filter/output` 三个处理流程中。

**数据类型**
- bool
`debug => true`
- string
`host => "hostname"`
- number
`port => 8080`
- array
`match => ["datetime", "UNIX", "ISO8601"]`
- hash
`options => { key1 => "value1", key2 => "value2" }`

> 在低于 1.2.0 的版本中，`hash` 语法跟 `array` 是一样的，比如：
`match => ["field1", "pattern1", "field2", "pattern2"]`

input 除了 stdin 外，还有 file、tcp、redis 等类型；filter 有很丰富的插件；output 除了 stdout 外，还有 file、Elasticsearch、redis、email等方式。甚至还可以自己写一个插件，所以具备良好的可扩展性。

**常用参数示例**
```
input {
    stdin {
        codec => "plain"
        tags => ["test"] #数组类型，一个事件可以有多个标签；在数据处理过程中，由具体的插件来添加或删除
        type => "std" #标记事件的唯一类型
    }
}

filter {
    #正则捕获；最好的解析非结构化日志，并结构化它们的工具；logstash 内置了120个匹配模式
    grok {
        #match => {"message" => "grok_pattern"}
        #WORD匹配字符串，NUMBER匹配int/float数值；将匹配的值赋给request_time
        match => {
        "message" => "%{WORD} %{NUMBER:request_time:float} %{WORD}"
        }
        #事件就是一个 Ruby 对象，可以随意给事件添加字段，或删除字段
        remove_field => ["message"] #再删除message字段
    }
    
    geoip {
        source => "client_ip" #source的值必须为公网IP，否则geoip不显示数据
        fields => ["city_name", "country_name", "location"] #指定的输出列
    }

    #将消息解析为json格式
    json { 
        source => "message"
    }

    date {
        match => {"logdate", "dd/MMM/yyyy:HH:mm:ss Z"}
    }
    
    if [type] == "std" {
        #do something
    }
}

output {
    stdout {
        codec => rubydebug
    }
    if "test" in [tags] {
        #do something
    }
}

```
## 2 Heka ##
采用了 `input-decoder-filter-encoder-output` 的日志处理流程，单个 Heka 服务内部的数据流通过 Message 数据模型在各个模块内流转。
Heka 内置了大多数模块插件，如 LogstreamerInput 以日志文件作为输入源，灵活的输入输出配置可以将分散各地的日志数据，收集和加工后统一输出到日志中心，Heka 进行统一编码后交给 ElasticSearch 存储。
#### 2.1 安装、运行 ####
源码安装较繁琐，建议用 rpm 包安装。
```
wget https://github.com/mozilla-services/heka/releases/download/v0.10.0/heka-0_10_0-linux-amd64.rpm
rpm -i heka-0_10_0-linux-amd64.rpm

hekad -version
```
新建配置文件，至少包括 input/encoder/output，就可以启动单个 Heka 服务。
```
heka -config xxx.toml
```
#### 2.2 配置文件 ####
TOML 格式：Tom's Obvious, Minimal Language
```
[HttpListenInput] #在配置端口启动一个http服务，将日志POST到该端口即可收集
address = "0.0.0.0:8325" #监听当前服务器的所有接口的8325端口
auth_type = "API" #接口认证方式为api,需要在请求头部加入X-API-KEY方可请求成功
api_key = "xxxx"

[accesslogs] #根据配置监控指定目录的指定日志文件，将变动的日志增量发送给Heka服务
type = "LogstreamerInput" 
#被监听日志文件目录 
log_directory = "/var/log/nginx" 
#正则匹配路径此处是匹配log_directory后面的路径,例如现在监听的文件路径为 #/var/log/nginx/2015/05/23/test.log 
file_match = '(?P<Year>\d+)/(?P<Month>\d+)/(?P<Day>\d+)/(?P<FileName>[^/]+)\.log' 
#排序,以match匹配到的年月日对文件进行排序依次监听读取 
priority = ["Year","Month","Day"] 
#日志的最后修改时间在oldest_duration时间后,则不会监听（heka 0.9.1及以前版本此处有bug,该设置无效） 
oldest_duration = "1h" 
#分类名设置,内部是修改全局变量 Logger,以备后面对日志流做来源区分,默认则为数据处理类名 
differentiator = ["FileName","-","access"]
decoder = "CombinedLogDecoder"
 
[CombinedLogDecoder] #将nginx日志和自己个性化的日志格式解码为标准的数据对象
type = "SandboxDecoder"
filename = "lua_decoders/nginx_access.lua"
    [CombinedLogDecoder.config]
    type = "combined"
    payload_keep = true
    user_agent_transform = true
    log_format = '$remote_addr - $remote_user'

[ESJsonEncoder] #将之前处理好的数据编码后，给后端的ElasticSearch使用
index = "%{Type}-%{%Y.%m.%d}" //设置写入ElasticSearch的索引值
es_index_from_timestamp = true
type_name = "%{Type}"//设置写入ElasticSearch的分类名
    [ESJsonEncoder.field_mappings]  //映射Heka内的数据键为es json格式的key值
    Timestamp = "@timestamp"
    Severity = "level"

[ElasticSearchOutput]
message_matcher = "Type == 'sync.log'" #设置过滤条件 无不需要过滤 设置为true即可
server = "http://es-server:9200" #ElasticSearch 服务地址
flush_interval = 5000 #刷新间隔
flush_count = 10 #刷新次数
encoder = "ESJsonEncoder" #指定编码插件
```

## 3 Logstash vs Heka ##
目前主流的后端日志，都采用标准的 elk 模式：Elasticsearch/Logstash/Kinaba，分别负责日志存储、日志收集、日志可视化；社区方面，Logstash 更成熟更健壮，能更快地解决遇到的问题。
如果日志文件多样，分布在不同的服务器，那么为了方便二次开发定制，可以采用 Heka 架构。
**简单示例比较**
- Logstash

```
input {
    file {
        path => "/var/log/nginx/access.log"
    }
}

output {
    stdout {}
}
```
- Heka

```
[LogstreamerInput]
log_directory="/var/log/nginx"
file_match='access.log'

[PayloadEncoder]
append_newlines = false

[LogOutput]
message_matcher = "TRUE"
encoder = "PayloadEncoder"
```
