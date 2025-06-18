from datetime import datetime

mood_responses = {
    "happy": "😊 That's awesome! Keep enjoying the good vibes.",
    "sad": "😢 Stay strong. Tomorrow is a new day.",
    "angry": "😠 Take a deep breath. Let it go.",
    "stressed": "🧘 Take a break. You've got this!"
}

mood = input("How are you feeling today? (happy/sad/angry/stressed): ").lower()
entry = input("Write something about your day: ")

filename = "journal.txt"
with open(filename, "a") as file:
    file.write(f"{datetime.now()} - Mood: {mood}\n{entry}\n\n")

print(mood_responses.get(mood, "📝 Entry saved. Stay mindful!"))