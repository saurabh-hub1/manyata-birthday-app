from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Poem text
poem = """To the One Who Lights My World

Today’s your day, my love, my light,
A star that makes my dark skies bright.
With every smile, with every touch,
You show me love, and oh, how much.

Your laughter is my favorite song,
With you, my heart feels right, feels strong.
Each moment shared, both big and small,
You're the most precious gift of all.

You bloom with grace, a rare delight,
More radiant than the moon at night.
No words can truly quite convey
The joy you bring me every day.

So on your birthday, here’s my vow:
To cherish you then, now, and how—
Forevermore, I’ll hold you dear,
With love that grows each passing year."""

# Quiz questions
questions = [
    ("What is Manyata’s favorite color?", "Pink"),
    ("Which song makes you think of her?", "Perfect"),
    ("How old is she turning today?", "21"),
    ("Who loves her the most?", "papa"),
]

# GUI App Class
class BirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Happy Birthday Manyata!")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffd6e8")  # Light pink background

        img = Image.open("manyata.jpeg")
        img = img.resize((200, 260))
        self.photo = ImageTk.PhotoImage(img)
        Label(root, image=self.photo, bg="#ffd6e8").pack(pady=10)

        Label(root, text="Happy 21st Birthday, Manyata!", font=("Brush Script MT", 28, "bold"),
              bg="#ffd6e8", fg="#d63384").pack()

        Button(root, text="Read Your Love Letter", command=self.show_poem,
               font=("Helvetica", 14), bg="#ff66b3", fg="white").pack(pady=10)

        Button(root, text="Play a Surprise Quiz!", command=self.start_quiz,
               font=("Helvetica", 14), bg="#ff3399", fg="white").pack(pady=10)

        Button(root, text="Exit", command=root.quit, font=("Helvetica", 12),
               bg="#ffb3d9", fg="black").pack(pady=20)

    def show_poem(self):
        messagebox.showinfo("To the One Who Lights My World", poem)

    def start_quiz(self):
        self.quiz_index = 0
        self.score = 0
        self.quiz_window()

    def quiz_window(self):
        if self.quiz_index < len(questions):
            q, _ = questions[self.quiz_index]
            self.q_window = Toplevel(self.root)
            self.q_window.geometry("400x200")
            self.q_window.title("Quiz Time!")
            Label(self.q_window, text=q, font=("Helvetica", 12)).pack(pady=10)
            self.answer_entry = Entry(self.q_window, font=("Helvetica", 12))
            self.answer_entry.pack(pady=5)
            Button(self.q_window, text="Submit", command=self.check_answer,
                   font=("Helvetica", 12)).pack(pady=10)
        else:
            self.show_final_message()

    def check_answer(self):
        user_ans = self.answer_entry.get().strip().lower()
        correct_ans = questions[self.quiz_index][1].strip().lower()
        if user_ans == correct_ans:
            self.score += 1
        self.q_window.destroy()
        self.quiz_index += 1
        self.quiz_window()

    def show_final_message(self):
        msg = f"Perfect Score! Just like us.\nYou got {self.score}/{len(questions)} right.\n\nHappy Birthday, Manyata!"
        messagebox.showinfo("You're Amazing!", msg)

# Launch
root = Tk()
app = BirthdayApp(root)
root.mainloop()