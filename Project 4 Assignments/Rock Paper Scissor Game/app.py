import random

print("🎮 Welcome to Rock, Paper, Scissors Game!")

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\n👉 Enter your choice (rock/paper/scissors): ").lower()
    if user_choice not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"💻 Computer chose: {computer_choice}")

    # 🔄 Result logic
    if user_choice == computer_choice:
        print("🤝 It's a Draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You Win!")
    else:
        print("😢 You Lose!")

    # 🔁 Play again?
    again = input("\n🔄 Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("👋 Thanks for playing!")
        break
