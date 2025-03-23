package main

import (
	"fmt"
	"math"
)

func sumWithForLoop(numbers []float64) float64 {
	sum := 0.0
	for _, num := range numbers {
		sum += num
	}
	return sum
}

// Taking the equation :  (sum + x) / (len + 1) = navg
// then x should be equal to (navg * (len + 1)) - sum
func NewAvg(arr []float64, navg float64) int64 {
	baseSum := sumWithForLoop(arr)
	lenArr := float64(len(arr))
	x := (navg * (lenArr + 1)) - baseSum
	if x <= 0 {
		return -1
	} else {
		return int64(math.Ceil(x))
	}
}
func main() {
	var a = []float64{14.0, 30.0, 5.0, 7.0, 9.0, 11.0, 16.0}
	res := NewAvg(a, 90) // Should return 628
	fmt.Println(res)
	a = []float64{14, 30, 5, 7, 9, 11, 15}
	res = NewAvg(a, 92) // Should return 645
	fmt.Println(res)
	a = []float64{1400.25, 30000.76, 5.56, 7, 9, 11, 15.48, 120.98}
	res = NewAvg(a, 2000) // Should return -1
	fmt.Println(res)
}
