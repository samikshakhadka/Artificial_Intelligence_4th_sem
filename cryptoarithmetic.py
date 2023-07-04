import itertools

def solve_cryptoarithmetic(equation):
    letters = set([char for char in equation if char.isalpha()])
    digits = range(10)
    for permutation in itertools.permutations(digits, len(letters)):
        digit_map = dict(zip(letters, permutation))
        if is_solution(equation, digit_map):
            return digit_map
    return None

def is_solution(equation, digit_map):
    left, right = equation.split('=')
    left_sum = sum(digit_map[char] * (10 ** (len(left) - 1 - i)) for i, char in enumerate(left) if char.isalpha())
    right_sum = sum(digit_map[char] * (10 ** (len(right) - 1 - i)) for i, char in enumerate(right) if char.isalpha())
    return left_sum == right_sum

def print_solution(digit_map):
    for letter, digit in digit_map.items():
        print(f"{letter}: {digit}")

equation = "SEND + MORE = SAMIKSHA"
solution = solve_cryptoarithmetic(equation)
if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution found.")
