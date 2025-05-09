package main

import "fmt"

type ISet[T comparable] interface {
	Has(item T) bool
	Add(item T) bool
	Remove(item T)
	Union(ISet[T]) ISet[T]
	Subset(ISet[T]) bool
	Difference(ISet[T]) ISet[T]
	Intersection(ISet[T]) ISet[T]
	Iter(yield func(T) bool)
	Clear()
	Size() int
}

type Set[T comparable] map[T]bool

func (s Set[T]) Has(item T) (ok bool) {
	_, ok = s[item]
	return
}
func (s Set[T]) Add(item T) bool {
	prev := len(s)
	s[item] = true
	return prev != len(s)
}
func (s Set[T]) Remove(e T) {
	delete(s, e)
}
func (s Set[T]) Iter(fc func(T) bool) {
	for k := range s {
		if !fc(k) {
			break
		}
	}
}
func (s Set[T]) Size() int {
	return len(s)
}
func (s Set[T]) Clear() {
	s = make(map[T]bool)
}
func (s Set[T]) Subset(set ISet[T]) bool {
	for v := range s {
		if !set.Has(v) {
			return false
		}
	}
	return true
}
func (s Set[T]) Intersection(set ISet[T]) ISet[T] {
	newSet := make(Set[T])
	for v := range s {
		if set.Has(v) {
			newSet.Add(v)
		}
	}
	return newSet
}
func (s Set[T]) Union(set ISet[T]) ISet[T] {
	newSet := make(Set[T])
	for v := range s {
		newSet.Add(v)
	}
	set.Iter(func(v T) bool {
		newSet.Add(v)
		return true
	})
	return newSet
}

func (s Set[T]) Difference(set ISet[T]) ISet[T] {
	newSet := make(Set[T])
	s.Iter(func(v T) bool {
		if !set.Has(v) {
			newSet.Add(v)
		}
		return true
	})
	set.Iter(func(v T) bool {
		if !s.Has(v) {
			newSet.Add(v)
		}
		return true
	})
	return newSet
}
func values[T comparable](s ISet[T]) []T {
	result := make([]T, 0, s.Size())
	s.Iter(func(item T) bool {
		result = append(result, item)
		return true
	})
	return result
}

func main() {
	setOne := make(Set[int])
	setTwo := make(Set[int])

	fmt.Println(setOne.Add(1)) // true
	fmt.Println(setOne.Add(1)) // false
	fmt.Println(setOne.Has(1)) // true

	setTwo.Add(1)
	setTwo.Add(2)
	setTwo.Add(3)

	setThree := setOne.Intersection(setTwo)
	fmt.Println(setThree.Size())  // 1
	fmt.Println(values(setThree)) // [1]

	setFour := setOne.Union(setTwo)
	fmt.Println(setFour.Size())  // 3
	fmt.Println(values(setFour)) // [1 2 3]

	fmt.Println(setOne.Subset(setFour)) // true

	setOne.Add(5) // now [1,5]

	fmt.Println(values(setFour.Difference(setOne))) // [2 3]

}
