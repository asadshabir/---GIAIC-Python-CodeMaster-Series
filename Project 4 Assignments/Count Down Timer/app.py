import time  # ⏰ Required for delay

# 🕒 Take time in seconds from user
t = int(input("⏳ Enter time in seconds: "))

while t > 0:
    mins, secs = divmod(t, 60)  # Convert into min:sec format
    timer = f'{mins:02d}:{secs:02d}'  # 00:00 format
    print(f"⏱️ Time Left: {timer}", end="\r")  # Show timer on same line
    time.sleep(1)  # Wait for 1 second
    t -= 1  # Decrease time

print("\n🔔 Time’s Up! Take a break or start again.")
