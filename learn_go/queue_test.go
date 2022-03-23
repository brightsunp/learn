package main

import (
    "os"
    "io/ioutil"
    "fmt"
    "path"
    "strconv"
    "testing"

    . "gopkg.in/check.v1"
)

func isExist(filename string) bool {
    _, err := os.Stat(filename)
    return err == nil || os.IsExist(err)
}

func putTestNums(q *queue, start int, end int) {
    for i := start; i <= end; i++ {
        q.Put([]byte(strconv.Itoa(i)))
    }
}

func EqualDepth(c *C, q *queue, expDepthMem int64, expDepthDisk int64) {
    c.Assert(q.DepthMem(), Equals, expDepthMem)
    c.Assert(q.DepthDisk(), Equals, expDepthDisk)
    expDepth := expDepthMem + expDepthDisk
    c.Assert(q.Depth(), Equals, expDepth)
}

type QueueSuite struct {}

var _ = Suite(&QueueSuite{})

func Test(t *testing.T) {
    TestingT(t)
}

// Run once when the suite starts running.
func (*QueueSuite) SetUpSuite(c *C) {
    fmt.Println("Queue tests begin...")
}

// Run once after all tests or benchmarks have finished running.
func (*QueueSuite) TearDownSuite(c *C) {
    fmt.Println("Queue tests finished.")
}

// Run before each test or benchmark starts running.
func (*QueueSuite) SetUpTest(c *C) {
    MemQueueConf.MaxMemSize = 10
    MemQueueConf.CheckCnt = 1
    MemQueueConf.StopQuantiles = 60
    MemQueueConf.RecoverQuantiles = 50

    DiskQueueConf.Dbname = "marco_access_log"
    DiskQueueConf.Dir = "./logger_db"
    DiskQueueConf.PerfileSize = 104857600
    DiskQueueConf.MaxMsgSize = 512000
    DiskQueueConf.SyncEvery = 2500
    DiskQueueConf.SyncTimeout = 2
}

// Run after each test or benchmark runs.
func (*QueueSuite) TearDownTest(c *C) {
    if q.DepthDisk() > 0 {
        q.Empty()
    }

    os.RemoveAll(DiskQueueConf.Dir)
}

func (*QueueSuite) TestBasic(c *C) {
    // test default config
    q = newQueue()
    c.Assert(q, NotNil)
    EqualDepth(c, q, 0, 0)
    
    
    msg := []byte("test")
    err := q.Put(msg)
    c.Assert(err, IsNil)
    EqualDepth(c, q, 1, 0)

    msgOut := <-q.ReadChan()
    c.Assert(string(msgOut), Equals, string(msg))
    EqualDepth(c, q, 0, 0)
}

func (*QueueSuite) TestConfigMemMax(c *C) {
    // test MemMax (MaxMemSize * StopQuantiles / 100)
    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 6, 4)
    q.Empty()

    MemQueueConf.StopQuantiles = 80

    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 8, 2)
}

func (*QueueSuite) TestConfigMemRecover(c *C) {
    // test MemRecover (MaxMemSize * RecoverQuantiles / 100)
    q = newQueue()
    putTestNums(q, 0, 10)
    q.Put([]byte("test"))
    EqualDepth(c, q, 6, 5)

    readChan := q.ReadChan()
    <-readChan
    <-readChan
    EqualDepth(c, q, 4, 5)

    q.Put([]byte("test"))
    EqualDepth(c, q, 5, 5)
}

func (*QueueSuite) TestConfigCheckCnt(c *C) {
    // test CheckCnt (check if MemMax by CheckCnt interval)
    MemQueueConf.CheckCnt = 10

    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 8, 2)
    q.Empty()

    MemQueueConf.CheckCnt = 5

    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 8, 2)
}

func (*QueueSuite) TestConfigDiskFile(c *C) {
    // test diskFile (Dbname & Dir)
    testDir, testDbname := "this_is_dir", "this_is_dbname"
    DiskQueueConf.Dir, DiskQueueConf.Dbname = testDir, testDbname

    q = newQueue()
    putTestNums(q, 0, 10)
    diskFile := fmt.Sprintf(path.Join(testDir, "%s.diskqueue.000000.dat"), testDbname)
    c.Assert(isExist(diskFile), Equals, true)
    q.Empty()
    c.Assert(isExist(diskFile), Equals, false)
}

func (*QueueSuite) TestConfigDiskFileSize(c *C) {
    // test diskFileSize (PerfileSize)
    DiskQueueConf.PerfileSize = 4

    q = newQueue()
    putTestNums(q, 0, 9)
    EqualDepth(c, q, 6, 3)

    diskFiles, _ := ioutil.ReadDir(DiskQueueConf.Dir)
    writeFileNum := len(diskFiles)
    c.Assert(writeFileNum, Equals, 4)
    for i := 0; i < writeFileNum-1; i++ {
        diskFile := diskFiles[i]
        c.Assert(diskFile.Size(), Equals, int64(5))
    }
}

func (*QueueSuite) TestConfigDiskMsgSize(c *C) {
    // test diskMsgSize (MaxMsgSize)
    MemQueueConf.StopQuantiles = 10
    MemQueueConf.RecoverQuantiles = 0
    testMsgSize := int32(3)
    DiskQueueConf.MaxMsgSize = testMsgSize

    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 1, 9)

    msg := []byte("test")
    err := q.Put(msg)
    errMsg := fmt.Sprintf("invalid message write size (%d) maxMsgSize=%d", len(msg), testMsgSize)
    c.Assert(err.Error(), Equals, errMsg)
    EqualDepth(c, q, 1, 9)
}

func (*QueueSuite) TestDelete(c *C) {
    // test Delete, diskFile remains, cannot Empty()
    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 6, 4)

    err := q.Delete()
    c.Assert(err, IsNil)
    EqualDepth(c, q, 6, 4)
    q.Empty()
    EqualDepth(c, q, 6, 4)
}

func (*QueueSuite) TestClose(c *C) {
    // test Close, diskFile remains, cannot Empty()
    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 6, 4)

    // when DepthMem > 0, flush memory to disk
    err := q.Close()
    c.Assert(err, IsNil)
    EqualDepth(c, q, 0, 10)

    // when DepthMem = 0
    err = q.Close()
    c.Assert(err, IsNil)
    EqualDepth(c, q, 0, 10)
    q.Empty()
    EqualDepth(c, q, 0, 10)
}

func (*QueueSuite) TestEmpty(c *C) {
    // test Empty, diskFile removed
    q = newQueue()
    putTestNums(q, 0, 10)
    EqualDepth(c, q, 6, 4)
    
    err := q.Empty()
    c.Assert(err, IsNil)
    EqualDepth(c, q, 6, 0)
}

func (*QueueSuite) TestOrderSingle(c *C) {
    // test read just once
    q = newQueue()
    go func() {
        putTestNums(q, 0, 2000)
    }()
    
    readChan := q.ReadChan()
    go func() {
        for j := 0; j < 2000; j++ {
            msg := <-readChan
            c.Assert(string(msg), Equals, strconv.Itoa(j))
        }
    }()
}

func (*QueueSuite) TestOrderMulti(c *C) {
    // test read multi times
    q = newQueue()
    go func() {
        putTestNums(q, 0, 1000)
    }()

    go func() {
        readChan := q.ReadChan()
        for j := 0; j < 500; j++ {
            msg := <-readChan
            c.Assert(string(msg), Equals, strconv.Itoa(j))
        }
    }()
    
    go func() {
        putTestNums(q, 1001, 2000)
    }()

    go func() {
        readChan := q.ReadChan()
        for j := 500; j < 1000; j++ {
            msg := <-readChan
            c.Assert(string(msg), Equals, strconv.Itoa(j))
        }
    }()
}
