# 🎉 Mad Libs Python Mini-Game 🎭

print("🌟 Welcome to the Mad Libs Game! 🌟\nFill in the blanks to create your own funny story! 🤪\n")

# 🔤 Inputs
name = input("👤 Enter a Name: ")
place = input("🌍 Enter a Place: ")
adjective = input("🎨 Enter an Adjective: ")
noun = input("📦 Enter a Noun: ")
verb = input("🏃 Enter a Verb: ")

# 📝 Displaying the story
print("\n📖 Here is your Mad Libs story:\n")
story = (
    f"One fine day, {name} went to {place}. 🧭\n"
    f"It was a really {adjective} place! 🌈\n"
    f"There, {name} found a mysterious {noun} 🧳 and decided to {verb} with it. 😄\n"
    "What a wild adventure! 🚀"
)

print("✨" * 50)
print(story)
print("✨" * 50)
