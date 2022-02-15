def calculate_pi(n_term: int) -> float:

    # initial conditions
    numerator: int = 4
    operation: int = 1
    denominator: int = 1
    pi: int = 0

    for _ in range(n_term):

        pi += operation * (numerator / denominator)
        operation *= -1
        denominator += 2

    return pi


if __name__ == '__main__':

    for n in range(1, 20001):

        pi = calculate_pi(n)
        print(f'Calculation with {n} terms: {round(pi, 6)}')