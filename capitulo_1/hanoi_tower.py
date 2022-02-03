from stack import Stack

num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

# init tower_a

for disc in range(1, num_discs + 1):

    tower_a.push(disc)

print(tower_a)