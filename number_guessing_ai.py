print("=== Number Guessing AI ===")
print("Think of a number between 1 and 100.")

low = 1
high = 100
attempts = 0

input("Press Enter when you're ready...")

while low <= high:
    guess = (low + high) // 2
    attempts += 1

    print(f"\nMy guess is: {guess}")
    feedback = input(
        "Is it (h)igher, (l)ower, or (c)orrect? "
    ).lower()

    if feedback == "c":
        print(f"\n🎉 I guessed your number in {attempts} attempts!")
        break

    elif feedback == "h":
        low = guess + 1

    elif feedback == "l":
        high = guess - 1

    else:
        print("Please enter h, l, or c.")
