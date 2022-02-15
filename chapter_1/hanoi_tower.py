from stack import Stack

# init tower_a

num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for disc in range(1, num_discs + 1):

    tower_a.push(disc)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:

    if n == 1:

        end.push(begin.pop())
    
    else:

        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)

if __name__ == '__main__':

    print(
        ('Inicial condition: \n'
        f'Tower A: {tower_a} \n'
        f'Tower B: {tower_b} \n'
        f'Tower C: {tower_c} \n')
    )

    hanoi(tower_a, tower_c, tower_b, num_discs)
    print('\n')    
    print(
        ('Final condition: \n'
        f'Tower A: {tower_a} \n'
        f'Tower B: {tower_b} \n'
        f'Tower C: {tower_c} \n')
    )

