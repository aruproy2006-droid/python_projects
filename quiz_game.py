score = 0

print("=== Python Quiz Game ===")

answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. Which planet is named after female deity ")
if answer.lower() == "venus":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What is ((((5 + 5)/5)*7)+53)? ")
if answer == "67":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuiz Finished!")
print("Your Score:", score, "/ 3")
