import time

print("1. Start     2. Quit")
print()
start = int(input("Enter your choice: "))
print()

if start == 1:
    name = input("Enter your name: ")
    print()
    print("Welcome to the game,", name)
    print()
    print("You may need a calculator to solve.")
    print()
    print("Follow these steps:")
    print()
    time.sleep(2)

    print("Step 1: Multiply your birth date by 2")
    print()
    time.sleep(5)

    print("Step 2: Add 5 to the result")
    print()
    time.sleep(5)

    print("Step 3: Multiply the result by 50")
    print()
    time.sleep(5)

    print("Step 4: Add your birth month number")
    print()
    time.sleep(5)

    print("Step 5: Subtract 250 from the result")
    print()
    time.sleep(5)

    print("Here is the result,", name, ":")
    print()
    time.sleep(2)

    print("The first one or two digits of your answer are your BIRTH DATE,")
    print("and the last two digits are your BIRTH MONTH.")

else:
    print("You chose to quit.")
