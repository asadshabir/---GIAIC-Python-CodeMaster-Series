'''🔹 Day 6 Challenge: Guess the Number Game 🎲'''

from random import randint

try:
    def play_again():
        print("🎯 I'm thinking of a number between 1 and 100...")
        randomNum = randint(1, 100)
        attempts = 1

        while True:
            try:
                user_inp = int(input("\t🤔 Take a guess: "))
                if user_inp > 100 or user_inp < 1:
                    print("\t⚠️ Please choose a number **between 1 and 100**!\n")
                    continue

                if user_inp == randomNum:
                    print("🎉 Correct guess! 🎉")
                    if attempts > 10:
                        print(f"🏁 You guessed the number {randomNum} in {attempts} attempts.")
                        print("😅 But you're not a master... yet.")
                    else:
                        print("🏆 YOU ARE A LEGEND!!")
                        print(f"💪 Guessed {randomNum} in just {attempts} attempts. Well played!\n")

                    again = input("🔁 Wanna play again? (Y/N): ").lower()
                    if again == "y":
                        print("\n🔄 Restarting game...\n")
                        play_again()
                    else:
                        print("\n👋 Thanks for playing! See you again.\n")
                    break

                elif user_inp > randomNum:
                    print("⬇️ Too High! Try a smaller number.")
                else:
                    print("⬆️ Too Low! Try a bigger number.")

                attempts += 1

            except ValueError:
                print("🚫 Invalid input! Please enter a number only.")

except Exception as e:
    print(f"❌ Error: {e}")

play_again()
