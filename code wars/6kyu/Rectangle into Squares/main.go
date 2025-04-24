package main

func SquaresInRect(lng int, wdth int) []int {
	var res []int
	if lng == wdth {
		return nil
	}
	for lng > 0 && wdth > 0 {
		if lng < wdth {
			res = append(res, lng)
			wdth = wdth - lng
		} else {
			res = append(res, wdth)
			lng = lng - wdth
		}
	}
	return res
}
func main() {
	SquaresInRect(5, 3)
}
