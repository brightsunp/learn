// The best way is to use the bytes package. It has a Buffer type which implements io.Writer.
package main

import (
    "bytes"
    "fmt"
)

func main() {
    var buffer bytes.Buffer

    for i := 0; i < 1000; i++ {
        buffer.WriteString("a")
    }

    fmt.Println(buffer.String())
}
// This does it in O(n) time.