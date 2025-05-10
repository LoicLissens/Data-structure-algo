from __future__ import annotations
from typing import Union, TypeVar, Generic

T = TypeVar("T")


class Set(Generic[T]):
    def __init__(self):
        self._storage = {}

    @property
    def values(self) -> list[T]:
        return [el for el in self._storage]

    def add(self, element: T):
        self._storage[element] = True

    def has(self, element: T) -> bool:
        return element in self

    def remove(self, element: T):
        if element in self._storage:
            del self._storage[element]
    def union(self, set: Set[T]) -> Set[T]:
        new_set =  Set[T]()
        for v in list(self)+list(set):
            new_set.add(v)
        return new_set

    def intersection(self,set: Set[T]) -> Set[T]:
        new_set =  Set[T]()
        for v in self:
            if set.has(v):
                new_set.add(v)
        return new_set
    def __contains__(self, element):
        return element in self._storage

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        return iter(self._storage)

def main():
    set_one = Set[int]()
    set_two = Set[int]()

    print(set_one.add(1))  # True
    print(set_one.add(1))  # False
    print(set_one.has(1))  # True

    set_two.add(1)
    set_two.add(2)
    set_two.add(3)

    set_three = set_one.intersection(set_two)
    print(len(set_three))     # 1
    print(set_three.values)    # [1]

    set_four = set_one.union(set_two)
    print(len(set_four))      # 3
    print(set_four.values)     # [1, 2, 3]

    print(set_one.subset(set_four))  # True

    set_one.add(5)  # now [1, 5]
    print(set_one.values)      # [1, 5]

if __name__ == "__main__":
    main()