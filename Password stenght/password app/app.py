# 🔐 Password Strength Checker - Decorated Version 💪
import streamlit 
import re
while True :
    def check_password_strength(password):
        print("\n🔍 Checking password strength...\n")
        score = 0

        # Length Check
        if len(password) >= 8:
            score += 1
            print("✅ Length is good (8+ characters)")
        else:
            print("❌ Password should be at least 8 characters long.")

        # Upper & Lowercase Check
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
            print("✅ Contains both uppercase and lowercase letters")
        else:
            print("❌ Include both uppercase and lowercase letters.")

        # Digit Check
        if re.search(r"\d", password):
            score += 1
            print("✅ Contains numbers (0-9)")
        else:
            print("❌ Add at least one number (0-9).")

        # Special Character Check
        if re.search(r"[!@#$%^&*]", password):
            score += 1
            print("✅ Includes special characters (!@#$%^&*)")
        else:
            print("❌ Include at least one special character (!@#$%^&*).")

        # Strength Rating
        print("\n📊 Password Strength Result:")
        if score == 4:
            print("💪 Very Strong Password! You're secure 🔐✅")
            exit()
        elif score == 3:
            print("⚠️ Moderate Password - Almost there! Add more strength 💡")
        else:
            print("🔓 Weak Password - Follow the suggestions above to improve 🔧")

    # 🚀 Get user input
    print("🔑 Welcome to the Password Strength Checker")
    password = input("📝 Enter your password: ")
    check_password_strength(password)
