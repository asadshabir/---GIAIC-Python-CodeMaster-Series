import random

print("🎯 Welcome to the Reverse Guessing Game!")
print("Think of a number between 1 and 100, and I (Computer 🤖) will try to guess it.")
input("Press Enter when you're ready... 😎\n")

low = 1
high = 100
attempts = 0

while True:
    guess = random.randint(low, high)
    attempts += 1
    print(f"\n🤔 My guess is: {guess}")
    feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

    if feedback == "c":
        print(f"\n🎉 Yayy! I guessed your number {guess} in {attempts} attempts! 🤖🎯")
        break
    elif feedback == "h":
        high = guess - 1
        print("📉 Okay, I'll guess lower...")
    elif feedback == "l":
        low = guess + 1
        print("📈 Got it, guessing higher...")
    else:
        print("❗ Invalid input! Please type H for high, L for low, or C for correct.")
