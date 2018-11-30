package main

import (
    "fmt"
    "time"
    "math/rand"
    "math"
)

func swap(x, y string) (string, string) {
    return y, x
}

func split(sum int) (x, y int) {
    x = sum*4/9
    y = sum - x
    return
}

func add(x, y int) int {
    return x + y
}

func main() {
    fmt.Println("Welcome to the playground!")
    fmt.Println("The time is", time.Now())
    fmt.Println("My favorite number is", rand.Intn(10))
    fmt.Printf("Now you have %g problems.\n", math.Sqrt(7))
    fmt.Println("42 + 13 =", add(42, 13))
    fmt.Println(swap("hello", "world"))
    fmt.Println(split(27))
}