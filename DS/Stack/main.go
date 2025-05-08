package main

import "fmt"

type IStack[T any] interface {
	Pop() (T, bool)
	Push(T)
	Peek() (T, bool)
	Length() int
}
type Stack[T any] struct {
	count   int
	storage map[int]T
}

func (stack *Stack[T]) Pop() (T, bool) {
	if stack.count == 0 {
		var zero T
		return zero, false
	}
	stack.count--
	res := stack.storage[stack.count]
	delete(stack.storage, stack.count)
	return res, true
}
func (stack *Stack[T]) Push(el T) {
	stack.storage[stack.count] = el
	stack.count++
}
func (stack *Stack[T]) Length() int {
	return stack.count
}
func (stack *Stack[T]) Peek() (T, bool) {
	if stack.count == 0 {
		var zero T
		return zero, false
	}
	return stack.storage[stack.count-1], true
}

func main() {
	var pal string = "racecar"
	var newStr string = ""
	var stack IStack[byte] = &Stack[byte]{storage: make(map[int]byte)}
	for _, char := range pal {
		stack.Push(byte(char))
	}
	fmt.Println(stack.Length()) // 7
	peek, _ := stack.Peek()
	fmt.Println(string(peek)) // r
	for stack.Length() > 0 {
		if r, ok := stack.Pop(); ok {
			newStr += string(r)
		}
	}
	fmt.Println(pal == newStr)
}
