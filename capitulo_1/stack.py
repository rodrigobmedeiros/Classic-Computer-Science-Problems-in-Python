from typing import TypeVar, Generic 

T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:

        self.items: list[T] = []

    def push(self, item: T) -> None:

        self.items.append(item)

    def pop(self) -> None:

        return self.items.pop()

    def empty(self) -> bool:

        return not self.items

    def __str__(self):

        return f'Stack({str(self.items)})'

if __name__ == '__main__':

    stack = Stack[int]()

    stack.push(1)
    stack.pop()