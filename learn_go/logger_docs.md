## logger 开发者文档 ##
CDN 边缘机器日志采集组件，负责采集边缘、中转机器的各种日志，并上报数据中心。
全局配置文件为`./etc/config.json`，里面的字段都开放给用户，可以个性化修改。
项目启动、初始化后，在`./src/main.go`中实现了以下几个功能模块。

#### 1 解析 error.log ####
入口函数`startLogConsumer`
在`error.go`的`logParser`结构体中，封装了整个处理过程的逻辑，主要方法有：
- `initConfig`——初始化配置 + 读取偏移量 + 根据日志类型选择对应的解析器。
- `produceLogInfo`——引入`go tail`，按偏移量读取日志直到文件末，并写入缓存。
- `parserLogLines`——调用`./src/parser/parser.go`中实现的日志解析器，解析缓存对应的日志结果。
- `postLogInfo`——将日志信息发送到配置的 HTTP 接口，默认不加`Content-Encoding: gzip`。
- `clearBufAndSaveOffset`——任务完成时清除缓存，并生成偏移量文件（以定位数据完整性）。

此模块中，`error.log`的内容不能是任意文本，每一行必须满足某种规则，否则会解析失败。
以`updns_error.log`为例：
```
2018-07-19T21:27:41+08:00 INFO query: 61.156.60.18#39868#6894 U ios-flydigi-com.b0.aicdn.com. IN A vm NO_ERROR NOERR:DONE 0 -/- CN-370000-2 1 0 CN-370000-2
```
对应的解析结果为：
```
{"@timestamp":"2018-07-19T21:27:41+08:00","client_country":"中国","client_errcode":"NO_ERROR","client_ip":"61.156.60.18","client_isp":"联通","client_port":"39868","client_province":"山东","client_region":"中国|山东|联通","discard":"0","edns":"-","id":"6894","in_errcode":"NOERR","in_state":"DONE","matched_country":"中国","matched_isp":"联通","matched_province":"山东","matched_region":"中国|山东|联通","matched_route_type":"empty","matched_rr_type":"A","node_host":"127.0.0.1","node_name":"localhost.localdomain","node_type":"updns","node_version":"v0.1.6.1","protocol":"U","qclass":"IN","qname":"ios-flydigi-com.b0.aicdn.com.","qtype":"A","scheduler_line":"vm","subnet":"-"}
```

#### 2 传输 nsq 日志 ####
入口函数`startNsqConsumer`
在`nsq.go`的`runConsumer`函数中，初始化配置，实现了拼接服务端 uri、选取 handler、连接 nsqd 失败则重连等功能。
在`handler.go`中，`PublishHandler`结构体的`HandleMessage`方法实现了处理 nsq 日志，`Publish`方法实现了定制化的发送日志方式：
POST 请求达到 100次 时，打印`send msg success`；结合`sink.go`中的`sender`处理，每隔 30s 执行一次 sender，每次发送 5个 worker，不考虑其他因素的话，实际效果是每隔 10min 打印一条发送成功的消息。

#### 3 传输 http 日志 ####
入口函数`startSink`
在`sink.go`的`sender`函数中，实现了 Queue 的核心功能：时间间隔达到`SinkConf.FlushInterval`，或内存达到`SinkConf.FlushSize`，或链表长度达到`SinkConf.FlushBatch`时，才会发送 POST 请求；在 http 日志的请求头中，添加了`X-Log-Type: marco_access`；如果连接数据中心失败的话，会每隔 1s 发起重新连接。

#### 4 监听 4500 端口 ####
入口函数`startHttpServer`和`stopHttpServer`，功能分别是打开和关闭 http server。该服务器实现了以下几个路由：
- `router.GET("/ping", ping_handler)`——返回状态码 200，响应体`{"message": "pong"}`
- `router.GET("/marco/depth", depth_handler)`——返回状态码 200，响应体`{"depth": q.Depth()}`
- `router.GET("/marco/depth/v2", depth_handler_v2)`——返回状态码 200，响应体`{"depth_mem": q.DepthMem(), "depth_disk": q.DepthDisk()}`
- `router.GET("/marco/sample", sample_handler)`——调用`sample.go`，持续一段时间把将接受的数据按照配置的日志格式写入指定文件供 debug 使用
- `router.POST("/marco/log", log_handler)`——接收 POST 请求，即第 3 节`传输 http 日志`的数据来源。
