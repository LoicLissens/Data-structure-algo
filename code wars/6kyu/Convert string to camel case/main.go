package kata

import "strings"

func ToCamelCase(s string) string {
	var result string
	var delimiter string
	if strings.Contains(s, "-") {
		delimiter = "-"
	}
	if strings.Contains(s, "_") {
		delimiter = "_"
	}
	splitted := strings.Split(s, delimiter)
	for i, str := range splitted {
		if i == 0 {
			result += str
		} else {
			result += strings.Title(str)
		}
	}
	return result
}
// real golfer do it this way

import (
	"regexp"
	"strings"
)

func ToCamelCase(s string) string {
	words := regexp.MustCompile("-|_").Split(s, -1)

	for i, w := range words[1:] {
		words[i+1] = strings.Title(w)
	}

	return strings.Join(words, "")
}