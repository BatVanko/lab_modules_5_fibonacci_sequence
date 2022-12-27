
def fibonacci_sequence(n):
    n1 = 0
    n2 = 1
    fibonacci_num = []
    if (n < 1):
        return
    fibonacci_num.append(n1)
    for i in range(1, n):
        fibonacci_num.append(n2)
        next_num = n1 + n2
        n1 = n2
        n2 = next_num
    return fibonacci_num


def print_sequence(num_list):
    print(' '.join(str(x) for x in num_list))


def create_number_from_list(f_sequence, num):
    if num in f_sequence:
        print(f"The number - {num} is at index {f_sequence.index(num)}")
    else:
        print(f"The number {num} is not in the sequence")
fibonacci_seq = []
while True:
    commands_line = input().split()

    if len(commands_line) == 3 and commands_line[0] == 'Create':
        count = int(commands_line[2])
        print_sequence(fibonacci_sequence(count))
        fibonacci_seq = fibonacci_sequence(count)
    elif len(commands_line) == 2 and commands_line[0] == 'Locate':
        wanted_number = int(commands_line[1])
        create_number_from_list(fibonacci_seq, wanted_number)
    elif commands_line == 'Stop':
        break
