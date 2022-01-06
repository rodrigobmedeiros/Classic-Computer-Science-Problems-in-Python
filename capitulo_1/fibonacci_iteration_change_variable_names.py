def fibonacci(n: int):

    if n == 1:
        return 0
    if n == 2:
        return 1

    n_2: int = 0
    n_1: int = 1

    for _ in range(3, n + 1):

        n_2, n_1 = n_1, n_1 + n_2

    return n_1

if __name__ == '__main__':

    print(fibonacci(5))