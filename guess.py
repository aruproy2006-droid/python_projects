import random

secret_number = random.randint(1, 10)
attempts = 0

print("🎮 Number Guessing Game")
print("Guess a number between 1 and 10")

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < 1 or guess > 10:
            print("⚠️ Enter a number between 1 and 10.")
            continue

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

        elif guess < secret_number:
            print("📉 Too low!")

        else:
            print("📈 Too high!")

    except ValueError:
        print("❌ Invalid input. Please enter a number.")
