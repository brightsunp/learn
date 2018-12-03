#### 1 Zabbix 协议 ####
Zabbix 使用自定义的、基于 TCP 的协议与客户端进行通信。
**协议内容**
```
<HEADER> ——数据头部，长度为 5bytes，内容为"ZBXD\x01"（0x01是协议版本 1HEX）
<DATA_LENGTH> ——数据长度，长度为 8bytes，内容为一个16进制的数字（1将格式化为01/00/00/00/00/00/00/00）
<DATA> ——数据内容，使用 json 格式；为了防止 Server 内存溢出，限定一次传输的数据不超过 128M
```

**Zabbix sender 协议**
```
<HEADER><DATALEN>{
    "request":"sender data",
    "data": [
        {
            "host": "Host name 1",
            "key": "item_key",
            "value": "33",
            "clock": 1381482894
        },
        {
            "host": "Host name 2",
            "key": "item_key",
            "value": "55",
            "clock":1381482905
        }
    ],
    "clock": 12143123
}

# Server response
<HEADER><DATALEN>{
    "response":"success",
    "info":"processed: 2; failed: 0; total: 2; seconds spent: 0.003534"
}
```

**Zabbix agent 协议**
```
# 被动检查：Server request & Agent response
<item key>\n

<HEADER><DATALEN><DATA>[\0<ERROR>]

# 主动检查：先获取相关 items 列表，关闭 TCP 连接，开始收集 items 的监控数据；收集完成后，再发送收集的数据到 server 中
# Agent request & Agent send & Server response
<HEADER><DATALEN>{
    "request":"active checks",
    "host":"<hostname>"
}

<HEADER><DATALEN>{
    "response":"success",
    "data":[
        {
            "key":"agent.version",
            "delay":600,
            "lastlogsize":0,
            "mtime":0
        },
        {
            "key":"vfs.fs.size[/nono]",
            "delay":600,
            "lastlogsize":0,
            "mtime":0
        }
    ]
}

<HEADER><DATALEN>{
    "request":"agent data",
    "data":[
        {
            "host":"<hostname>",
            "key":"agent.version",
            "value":"2.4.0",
            "clock":1400675595,
            "ns":76808644
        },
        {
            "host":"<hostname>",
            "key":"vfs.fs.size[/nono]",
            "state":1,
            "value":"Cannot obtain filesystem information: [2] No such file or directory",
            "clock":1400675595,
            "ns":78154128
        }
    ],
    "clock": 1400675595,
    "ns": 78211329
}

<HEADER><DATALEN>{
    "response":"success",
    "info":"processed: 2; failed: 0; total: 2; seconds spent: 0.003534"
}
```
#### 2 Zabbix API 接口 ####
Zabbix API提供了很多方法，当用户的身份验证通过收集令牌后，就可以对Zabbix对象进行很多不同类型的操作。
Zabbix API采用JSON-RPC协议，意味着调用任何方法都需要发送POST请求，输入或输出JSON格式的数据。

> HTTP 报头中，Content-Type必须设置为application/json、application/json-rpc或者application/jsonrequest）

大部分APIs都包含 get/create/update/delete 4个方法，具体的使用方法可查询文档：[https://www.zabbix.com/documentation/3.4/manual/api/reference](https://www.zabbix.com/documentation/3.4/manual/api/reference "Zabbix APIs")。
