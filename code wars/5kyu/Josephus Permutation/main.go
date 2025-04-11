package kata

func RemoveIndex(s []interface{}, index int) []interface{} {
	ret := make([]interface{}, 0)
	ret = append(ret, s[:index]...)
	return append(ret, s[index+1:]...)
}

func Josephus(items []interface{}, k int) []interface{} {
	if len(items) == 0 {
		return items
	}
	if k == 1 {
		return items
	}
	var result []interface{} = make([]interface{}, 0)
	var index int = 0
	for len(items) > 0 {
		index = (index + k - 1) % len(items)
		result = append(result, items[index])
		items = RemoveIndex(items, index)
	}
	return result
}

// golfed:

func JosephusGolfed(items []interface{}, k int) []interface{} {
	p := 0
	result := []interface{}{}
	for len(items) > 0 {
		p = ((p + k - 1) % len(items))
		result = append(result, items[p])
		items = append(items[:p], items[p+1:]...)
	}
	return result
}
