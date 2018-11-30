package main

import (
    "fmt"
    "math"
    "runtime"
    "time"
)

func when_sat() string {
	switch today:=time.Now().Weekday(); time.Saturday {
	case today + 0:
		return "Today."
	case today + 1:
		return "Tomorrow."
	case today + 2:
		return "In two days."
	default:
		return "Too far away."
	}
}

func get_os() string {
    switch os:=runtime.GOOS; os {
    case "darwin":
        return "OS X."
    case "linux":
        return "Linux."
    default:
        // freebsd, openbsd, plan9, windows...
        return os + "."
    }
}

func sqrt_all(x float64) string {
    if x<0 {
        return sqrt_all(-x) + "i"
    }
    return fmt.Sprint(math.Sqrt(x))
}

func main() {
    sum := 0
    for i:=0; i<10; i++ {
        sum +=i
    }
    fmt.Println(sum)
    
    sum = 1
    for sum < 1000 {
        sum += sum
    }
    fmt.Println(sum)
    
    fmt.Println(sqrt_all(-3), sqrt_all(4))
    fmt.Println(get_os())
    fmt.Println("When is Saturday?", when_sat())
    
    fmt.Println("Counting...")
    for i:=0; i<10; i++ {
        defer fmt.Println(i)
    }
    fmt.Println("Done")
}