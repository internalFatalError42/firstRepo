
def normal_close_example():
    class A:
        v = 42

        def __init__(self):
            self.x = 42
            self.y = 43
            self.z = 44

    a = A()
    print(a.__dict__)

    class B:
        __slots__ = 'x', 'y', 'z'

        def __init__(self):
            self.x = 42
            self.y = 43
            self.z = 44

    b = B()
    print(b.__dict__)


def main():
    normal_close_example()


if __name__ == "__main__":
    main()
