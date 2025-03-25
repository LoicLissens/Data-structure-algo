package kata

func count(slice []rune, el rune) int {
	count := 0
	for _, s := range slice {
		if s == el {
			count++
		}
	}
	return count
}

func IsValidWalk(walk []rune) bool {
	var length int = len(walk)
	if length != 10 || length%2 != 0 {
		return false
	}
	if count(walk, 'n') == count(walk, 's') && count(walk, 'w') == count(walk, 'e') {
		return true
	}
	return false

}
