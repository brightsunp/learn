package main

import (
    "fmt"
    "math"
    "time"
)

type MyError struct {
	When time.Time
	What string
}

func (e *MyError) Error() string {
	return fmt.Sprintf("at %v, %s",
		e.When, e.What)
}

func run() error {
	return &MyError{
		time.Now(),
		"it didn't work",
	}
}

type Abser interface {
    Abs() float64
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

type Vertex struct {
    X, Y float64
}

func (v *Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
    // struct type
    v := Vertex{3, 4}
    fmt.Println(v.Abs())
    
    // non-struct type
    f := MyFloat(-6)
    fmt.Println(f.Abs())
    
    // interface
    var a Abser
    a = f
    a = &v
    fmt.Println(a.Abs())
    
    // interface value
    var i interface{} = "hello"
    s, ok := i.(string)
    fmt.Println(s, ok)
    s1, ok := i.(float64)
    fmt.Println(s1, ok)
    // keyword: type (switch)
    switch t := i.(type) {
        case string:
            fmt.Printf("%q is %v bytes long\n", t, len(t))
        default:
            fmt.Printf("%v, %T", t, t)
    }
    
    // error
    if err:=run(); err!=nil {
        fmt.Println(err)
    }
}