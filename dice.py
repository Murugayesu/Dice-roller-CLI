import random

def program():
    print("🎲 Welcome to the Dice Roller!")
    while True:
        sides = input("Enter the number of sides on the die (or 'q' to quit): ")
        if sides == 'q':
            break
        try:
            sides = int(sides)
            if sides < 2:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a positive integer more than 1.")
            continue
        print(f"Rolling... 🎲")
        roll = random.randint(1, sides)
        print(f"You got : {roll}")
        print("🎲 Roll again? (Press Enter to continue or 'q' to quit)")
        again = input()
        if again == 'q':
            break
if __name__ == "__main__":
    program()