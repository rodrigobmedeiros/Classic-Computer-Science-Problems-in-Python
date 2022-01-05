def fibonacci(n: int):

    if n == 1:
        return 0
    if n == 2:
        return 1

    last: int = 0
    next: int = 1

    for _ in range(3, n + 1):
        print(last)
        print(next)
        last, next = next, next + last

        print(last)
        print(next)

    return next

if __name__ == '__main__':

    print(fibonacci(4))