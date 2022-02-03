from typing import TypeVar, Generic, List


# create a generic type to be used into class construction
T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:

        self._container: List[T] = []

    def push(self, item: T) -> None:

        self._container.append(item)

    def pop(self) -> T:

        return self._container.pop()

    def __repr__(self) -> None:

        return repr(self._container)

if __name__ == '__main__':

    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)