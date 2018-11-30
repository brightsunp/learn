package main

import (
	"fmt"
	"time"
    "sync"
)

// SafeCounter is safe to use concurrently.
type SafeCounter struct {
	v   map[string]int
	mux sync.Mutex
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string) {
	c.mux.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	c.v[key]++
	c.mux.Unlock()
}

// Value returns the current value of the counter for the given key.
func (c *SafeCounter) Value(key string) int {
	c.mux.Lock()
	// defer: ensure mutex will be unlocked.
	defer c.mux.Unlock()
	return c.v[key]
}

func fibonacci1(c, quit chan int) {
    // args: c, quit both channels
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum //send sum to c
}

func main() {
	s := []int{7, 2, 8, -9, 4, 0}
    
    // channel
    c := make(chan int) // created before use
    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    a, b := <-c, <-c // receive from c
    fmt.Println(a, b, a+b)
    
    // buffered channel: range util closed
    ch := make(chan int, 10)
	go fibonacci(cap(ch), ch)
	for i := range ch {
		fmt.Println(i)
	}
    
    // select block
    c1 := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c1)
		}
		quit <- 0
	}()
	fibonacci1(c1, quit)
    
    // default selection
    tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)
	for {
		select {
		case <-tick:
			fmt.Println("tick.")
		case <-boom:
			fmt.Println("BOOM!")
			return
		default:
			fmt.Println("    .")
			time.Sleep(50 * time.Millisecond)
		}
	}
    
    // sync.Mutex
    sc := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 1000; i++ {
		go sc.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(sc.Value("somekey"))
}
