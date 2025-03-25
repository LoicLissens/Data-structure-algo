package kata

import (
	"strconv"
	"strings"
)

func NbDig(n int, d int) int {
	count := 0
	for i := 0; i <= n+1; i++ {
		arr := strings.Split(strconv.Itoa(i*i), "")
		for _, v := range arr {
			if v == strconv.Itoa(d) {
				count++
			}
		}
	}
	return count
}

// Can be golfed like this (saw on code wars)

func NbDigTwo(n int, d int) (out int) {
	for i := 0; i <= n; i++ {
		out += strings.Count(strconv.Itoa(i*i), strconv.Itoa(d))
	}

	return
}
