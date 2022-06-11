import inspect
import sys
from dataclasses import dataclass, field
from pprint import pprint


class C:
    def __init__(self):
        self.__x: str = "hello"
        self.__y: int = 1

    def x(self) -> str:
        return self.__x

    def y(self) -> int:
        return self.__y


class D:
    __slots__ = ('__x', '__y')

    def __init__(self):
        self.__x: str = "hello"
        self.__y: int = 1

    def y(self) -> int:
        return self.__y


class E(D):
    pass


# source:  https://www.youtube.com/watch?v=vBH6GRJ1REM
@dataclass(frozen=True, order=True)
class Comment:
    id: int = field()
    text: str = field(default='')
    replies: list[int] = field(default_factory=list, compare=False, hash=False, repr=False)


def main():
    #print(C())
    #print(sys.getsizeof(C()))
    #print(C().__dict__)

    #print(D())
    #print(sys.getsizeof(D()))
    #print(D().y())

    #print(E())
    #print(sys.getsizeof(E()))
    #print(E().__dict__)
    print("_______________")

    comment = Comment(1, "I just subscribed!")
    print(comment.__dict__)
    pprint(inspect.getmembers((Comment, inspect.isfunction)))


if __name__ == "__main__":
    main()
