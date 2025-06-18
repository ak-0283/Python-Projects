import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

# Mood responses dictionary
mood_responses = {
    "happy": "😊 That's awesome! Keep enjoying the good vibes.",
    "sad": "😢 Stay strong. Tomorrow is a new day.",
    "angry": "😠 Take a deep breath. Let it go.",
    "stressed": "🧘 Take a break. You've got this!"
}

# Set up the appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MoodJournalApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mood Journal")
        self.geometry("500x400")

        # Placeholder tracking
        self.placeholder = "Type something here..."
        self.placeholder_active = True

        # Title label
        self.title_label = ctk.CTkLabel(
            self, text="How are you feeling today?", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=20)

        # Mood dropdown
        self.mood_option = ctk.CTkOptionMenu(self, values=list(mood_responses.keys()))
        self.mood_option.pack(pady=10)

        # Textbox for journal entry
        self.entry_box = ctk.CTkTextbox(self, height=150)
        self.entry_box.pack(padx=20, pady=10, fill="both", expand=True)
        self.entry_box.insert("1.0", self.placeholder)
        self.entry_box.bind("<FocusIn>", self.clear_placeholder)
        self.entry_box.bind("<FocusOut>", self.restore_placeholder)

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.save_entry)
        self.submit_button.pack(pady=10)

        # Feedback label
        self.feedback_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.feedback_label.pack(pady=10)

    def clear_placeholder(self, event=None):
        if self.placeholder_active:
            self.entry_box.delete("1.0", "end")
            self.placeholder_active = False

    def restore_placeholder(self, event=None):
        if not self.entry_box.get("1.0", "end").strip():
            self.entry_box.insert("1.0", self.placeholder)
            self.placeholder_active = True

    def save_entry(self):
        mood = self.mood_option.get().lower()
        entry = self.entry_box.get("1.0", "end").strip()

        if not entry or self.placeholder_active:
            messagebox.showwarning("Empty Entry", "Please write something about your day.")
            return

        with open("journal.txt", "a") as file:
            file.write(f"{datetime.now()} - Mood: {mood}\n{entry}\n\n")

        response = mood_responses.get(mood, "📝 Entry saved. Stay mindful!")
        self.feedback_label.configure(text=response)
        self.entry_box.delete("1.0", "end")
        self.restore_placeholder()


if __name__ == "__main__":
    app = MoodJournalApp()
    app.mainloop()