package main

import (
	"fmt"
	"reflect"
	"sort"
)

func comp(array1 []int, array2 []int) bool {
	if len(array1) != len(array2) {
		return false
	}
	if array1 == nil || array2 == nil {
		return false
	}
	array3 := make([]int, len(array1))
	for i, v := range array1 {
		array3[i] = v * v
	}
	sort.Slice(array2, func(i, j int) bool {
		return array2[i] < array2[j]
	})
	sort.Slice(array3, func(i, j int) bool {
		return array3[i] < array3[j]
	})
	for i, v := range array2 {
		if v != array3[i] {
			return false
		}
	}
	return true
}

// Can be goldfed this way with reflect
func CompGolfed(a, b []int) bool {
	if a == nil || b == nil {
		return false
	}

	c, d := a[:], b[:]
	for i, n := range a {
		c[i] = n * n
	}

	sort.Ints(c)
	sort.Ints(d)
	return reflect.DeepEqual(c, d)
}

// optimal sol
func CompMax(array1 []int, array2 []int) bool {
	if array1 == nil || array2 == nil {
		return false
	}
	if len(array1) != len(array2) {
		return false
	}
	if len(array1) == 0 {
		return true
	}
	firstCalc := make(map[int]int)
	for _, v := range array1 {
		firstCalc[v*v]++
	}

	for _, v := range array2 {
		kv, ok := firstCalc[v]
		if ok == false || kv == 0 {
			return false
		}
		firstCalc[v]--
	}
	return true
}
func main() {
	var a1 = []int{121, 144, 19, 161, 19, 144, 19, 11}
	var a2 = []int{11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19}
	bool := CompMax(a1, a2)
	fmt.Println(bool)
}
