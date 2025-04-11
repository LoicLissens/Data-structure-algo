package kata

package main

import (
    "slices"
)

func main() {
    letters := []string{"a", "b", "c", "d", "e"}
    letters = slices.Delete(letters, 1, 4)
    fmt.Println(letters)
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
    result = append(result,items[index])
    slices.Delete(items, index, 1)
  }
}