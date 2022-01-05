# Fibonacci sequence implemented in recurcive way
from typing import Dict

# definição dos elementos base
memo: Dict[int, int] = {1: 0, 2:1}

def fibonacci(n: int) -> int:

    if n not in memo:

        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]

if __name__ == '__main__':
    print(memo)
    print(fibonacci(3))

    print(memo)
    print(fibonacci(10))

    print(memo)
    print(fibonacci(50))

    print(memo)