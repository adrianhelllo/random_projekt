import random

VALUES = {
    '🍎': 0.5,
    '🍏': 0.6,
    '🍋': 0.7,
    '🍐': 0.9,
    '🍊': 1,
    '🍑': 1.2,
    '🍒': 1.5,
    '💸': 1.7,
    '💰': 2,
}

width = 15

def welcome_msg():
    sep = '-' * width
    print("Welcome to my slot-machine program!")
    print("You will be able to bet on 1, 2 or 3 lines of the slot machine, which will each multiply your bet, based on what they land on.")
    print(f"Here are all the possible outcomes and their multipliers:")
    print(f'\n{sep}\n'.join(f'{f"{key} -> {value}":^{width}}' for key, value in VALUES.items()))
    bal = input("Please enter your starter balance to begin with [bal > 0]: ")
    while not (bal > 0):
        print("Invalid input. Please try again.")
        bal = input("Please enter your starter balance to begin with [bal > 0]: ")
    return bal

def print_slots(on):
    chosen_multips = [random.choice(list(VALUES.keys())) for _ in range(3)]
    line = (
    f"| {random.choice(chosen_multips) if on else '  '} | "
    f"{random.choice(chosen_multips) if on else '  '} | "
    f"{random.choice(chosen_multips) if on else '  '} |"
    )
    print(f'{"----------------":^{width}}')
    print(f"{line:^{width}}")
    print(f'{"----------------":^{width}}')

def main():
    bal = welcome_msg()
    print_slots(False)
    print("Type pull")

if __name__ == '__main__':
    main()

