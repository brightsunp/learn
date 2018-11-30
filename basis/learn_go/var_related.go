package main

import (
    "fmt"
    "strings"
    "math"
)

func fibonacci() func() int {
    a, b := 0, 1
    return func() int {
        a, b = b, a+b
        return a
    }
}

func compute(fn func(float64, float64) float64) float64 {
    return fn(3, 4)
}

type Vertex struct {
    X, Y int
}

func main() {
    // pointer
    i := 2701
    p := &i
    fmt.Println(*p)
    *p /= 37
    fmt.Println(i)
    
    // struct
    v1 := Vertex{1, 2}
    v2 := Vertex{X: 1}
    q := &Vertex{1, 2}
    fmt.Println(v1, v2, q)
    
    // array & slice
    a := [10]string{"Hello", "World", "Three"}
    b := []Vertex{{1, 2}, {3, 4}}
    fmt.Println(a[1:3])
    fmt.Println(b)
    
    // slice of slices
    board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}
	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
        // fmt.Println(board[i])
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
    
    // map
    m := map[string]Vertex{
        "first": {1, 2},
        "second": {3, 4},
    }
    elem, ok := m["first"]
    fmt.Println(elem, ok)
    elem, ok = m["fi"]
    fmt.Println(elem, ok)
    
    // func as value
    fmt.Println(compute(math.Pow))
    
    // closure: fibonacci is a function that returns a function that returns an int.
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}

}   
