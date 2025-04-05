package kata

import (
	"fmt"
	"strings"
)

func TowerBuilder(nFloors int) []string {
	tower := make([]string, nFloors)
	for i := 0; i < nFloors; i++ {
		spaces := nFloors - i - 1
		stars := 2*i + 1
		tower[i] = fmt.Sprint(strings.Repeat(" ", spaces), strings.Repeat("*", stars), strings.Repeat(" ", spaces))
	}
	return tower
}

// Without fmt
func TowerBuilderTwo(nFloors int) []string {
	tow := make([]string, nFloors)
	for i := 0; i < nFloors; i++ {
		spaces := strings.Repeat(" ", nFloors-(i+1))
		blocks := strings.Repeat("*", i*2+1)
		tow[i] = spaces + blocks + spaces
	}
	return tow
}
