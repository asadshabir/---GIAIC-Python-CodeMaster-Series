import random

# 🔤 List of words
words = ["python", "hangman", "challenge", "banana", "laptop", "giraffe"]
word = random.choice(words)  # 🎯 Random word
word_letters = list(word)
guessed_letters = []
lives = 6  # ❤️ 6 chances

print("🎮 Welcome to Hangman Game!")
print("Guess the word, one letter at a time! ✍️")

# 🔁 Game loop
while lives > 0:
    display_word = ""

    # 🔍 Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\n🔤 Word: ", display_word.strip())
    print(f"❤️ Lives left: {lives}")
    guess = input("👉 Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        print("✅ Good guess!")
        word_letters = [l for l in word_letters if l != guess]
    else:
        print("❌ Wrong guess!")
        lives -= 1

    # 🎉 Win condition
    if set(guessed_letters) >= set(word):
        print(f"\n🎉 Congrats! You guessed the word: {word.upper()}")
        break

# 💀 Lose condition
if lives == 0:
    print(f"\n💀 Game Over! The word was: {word.upper()}")
