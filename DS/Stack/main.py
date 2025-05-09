from typing import Union,TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._count = 0
        self.storage: dict[int,T] =  {}

    @property
    def length(self)-> int:
        return self._count
    @staticmethod
    def pop(self) -> Union[T,None]:
        if self._count == 0:
            return None
        self._count -= 1
        res =  self.storage[self._count]
        self.storage.pop(self._count) # lol
        return res

    def push(self,el: T):
        self.storage[self._count] = el
        self._count += 1

    def peek(self) -> Union[T,None]:
        if self._count == 0:
            return None
        return self.storage[self._count-1]

def main():
    pal = "racecar"
    new_str = ""
    my_stack =  Stack[str]()
    for char in pal:
        my_stack.push(char)
    print(my_stack.length) #7
    print(my_stack.peek()) # r
    for char in pal:
        new_str += my_stack.pop()
    assert pal == new_str
if __name__ == "__main__":
    main()
