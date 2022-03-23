package main

import (
    "encoding/binary"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net"
    "time"
    "strings"
)

// ZabbixConfObj ...
type ZabbixConfObj struct {
    AgentHosts      []string
    ProxyHost       string
    ServerHost      string
    AgentPort       int
    ServerPort      int
}

// ZabbixConf ... load config.json
var ZabbixConf = ZabbixConfObj{
    []string{"agenthost"},
    "proxyhost",
    "serverhost",
    10050,
    10051,
}

// ZabbixHandler ...
type ZabbixHandler struct {
    Host    string
    Port    int
}

// Method ZabbixHandler class, return zabbix header.
func (z *ZabbixHandler) getHeader() []byte {
    return []byte("ZBXD\x01")
}

// Method ZabbixHandler class, return data length.
func (z *ZabbixHandler) getDataLen(data []byte) []byte {
    dataLen := make([]byte, 8)
    binary.LittleEndian.PutUint32(dataLen, uint32(len(data)))
    return dataLen
}

// Method ZabbixHandler class, resolve uri by hostname:port.
func (z *ZabbixHandler) getTCPAddr() (iaddr *net.TCPAddr, err error) {
    addr := fmt.Sprintf("%s:%d", z.Host, z.Port)

    // Resolve hostname:port to ip:port
    iaddr, err = net.ResolveTCPAddr("tcp", addr)
    if err != nil {
        err = fmt.Errorf("Connection failed: %s", err.Error())
    }

    return
}

// Method ZabbixHandler class, make connection to uri.
func (z *ZabbixHandler) connect() (conn *net.TCPConn, err error) {
    type DialResp struct {
        Conn  *net.TCPConn
        Error error
    }

    // Open connection to zabbix host
    iaddr, err := z.getTCPAddr()
    if err != nil {
        return
    }

    // dial tcp and handle timeouts
    ch := make(chan DialResp)

    go func() {
        conn, err = net.DialTCP("tcp", nil, iaddr)
        ch <- DialResp{Conn: conn, Error: err}
    }()

    select {
    case <-time.After(5 * time.Second):
        err = fmt.Errorf("Connection Timeout")
    case resp := <-ch:
        if resp.Error != nil {
            err = resp.Error
            break
        }

        conn = resp.Conn
    }

    return
}

// Read data from connection.
func (z *ZabbixHandler) Read() (res []byte, err error) {
    conn, err := z.connect()
    if err != nil {
        return
    }
    defer conn.Close()
    
    res = make([]byte, 1024)
    res, err = ioutil.ReadAll(conn)
    if err != nil {
        err = fmt.Errorf("Error while receiving the data: %s", err.Error())
    }

    return
}

// Send packet to zabbix.
func (z *ZabbixHandler) Send(data []byte) (res []byte, err error) {
    conn, err := z.connect()
    if err != nil {
        return
    }
    defer conn.Close()

    /*
       fmt.Printf("HEADER: % x (%s)\n", z.getHeader(), z.getHeader())
       fmt.Printf("DATALEN: % x, %d byte\n", z.getDataLen(data), len(z.getDataLen(data)))
       fmt.Printf("BODY: %s\n", string(data))
    */

    // Fill buffer
    buffer := append(z.getHeader(), z.getDataLen(data)...)
    buffer = append(buffer, data...)

    // Sent packet to zabbix
    _, err = conn.Write(buffer)
    if err != nil {
        err = fmt.Errorf("Error while sending the data: %s", err.Error())
        return
    }

    res = make([]byte, 1024)
    res, err = ioutil.ReadAll(conn)
    if err != nil {
        err = fmt.Errorf("Error while receiving the data: %s", err.Error())
    }

    return
}

func splitMsg(msg []byte) (req string, data []byte) {
    // subslice from [total length of header and dataLenth] to end
    data = msg[13:]

    m := make(map[string] interface{})
    json.Unmarshal(data, &m)

    if temp, ok := m["request"]; ok {
        // req in {"active", "agent", "sender"}
        req = strings.Split(temp.(string), " ")[0]
    } else {
        req = "response"
    }

    return
}

func runZabbix(agentHost string, zabbixQueue *queue) {
    wg.Add(1)
    defer wg.Done()
    
    agentHandler := &ZabbixHandler{agentHost, ZabbixConf.AgentPort}
    proxyHandler := &ZabbixHandler{ZabbixConf.ProxyHost, ZabbixConf.ServerPort}
    serverHandler := &ZabbixHandler{ZabbixConf.ServerHost, ZabbixConf.ServerPort}

    Log.Info("zabbix consumer agent:%s:%d start ...", agentHost, ZabbixConf.AgentPort)
    // process agent data every 2 seconds
    ticker := time.NewTicker(2 * time.Second)
	flush := false
    for {
        flush = false

        select {
        case <-ticker.C:
            flush = true
        case <-done:
            Log.Info("zabbix consumer agent:%s:%d stop ...", agentHost, ZabbixConf.AgentPort)
            return
        }

        if !flush {
            continue
        }

        // read agent query
        temp, _ := agentHandler.Read()
        if temp == nil {
            continue
        }
        req, data := splitMsg(temp)

        if req == "active" {
            // send query to server
            temp, _ = serverHandler.Send(data)
            req, data = splitMsg(temp)
            if req != "response" {
                Log.Error("no response from zabbix server: %s:%d", ZabbixConf.ServerHost, ZabbixConf.ServerPort)
                continue
            }

            // send res to agent
            agentHandler.Send(data)
        } else {
            // send realtime data to proxy
            _, err := proxyHandler.Send(data)
            if err != nil {
                // reserve data to diskqueue
                Log.Error("connect to zabbix proxy (%v) failed: %s:%d", err, ZabbixConf.ProxyHost, ZabbixConf.ServerPort)
                zabbixQueue.Put(data)
                continue
            }
            
            // send zabbixQueue data to proxy
            for {
                select {
                case readChan := <-zabbixQueue.ReadChan():
                    proxyHandler.Send(readChan)
                default:
                    break
                }
            }
        }
    }
}

func startZabbixConsumer() {
    zabbixQueue := newQueue()
    defer zabbixQueue.Close()

    for _, agent := range ZabbixConf.AgentHosts {
        go runZabbix(agent, zabbixQueue)
    }
}
