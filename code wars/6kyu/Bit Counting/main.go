package main

func CountBits(n uint) int {
	count := 0
	for n > 0 {
		count += int(n & 1)
		n >>= 1
	}
	return count
}
// real OG do it this way
import "math/bits"
var CountBits = bits.OnesCount