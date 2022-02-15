# Fibonacci sequence implemented in recurcive way


def fibonacci(n: int) -> int:

    if n <= 2:
        return n - 1

    fib_n = fibonacci(n - 1) + fibonacci(n - 2)

    return fib_n

if __name__ == '__main__':

    print(fibonacci(1))