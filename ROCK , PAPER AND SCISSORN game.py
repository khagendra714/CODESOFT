import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("520x600")
root.configure(bg="#0f172a")

choices = ["🪨", "📄", "✂"]
names = {"🪨": "Rock", "📄": "Paper", "✂": "Scissors"}

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_display.config(text=user_choice, font=("Arial", 50))
    comp_display.config(text=computer_choice, font=("Arial", 50))

    user = names[user_choice]
    comp = names[computer_choice]

    if user == comp:
        result = "It's a Tie 🤝"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Scissors" and comp == "Paper") or \
         (user == "Paper" and comp == "Rock"):
        result = "You Win 🎉"
        user_score += 1
    else:
        result = "Computer Wins 💻"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"You: {user_score}   Computer: {computer_score}"
    )

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_display.config(text="")
    comp_display.config(text="")
    result_label.config(text="")
    score_label.config(text="You: 0   Computer: 0")

title = tk.Label(root, text="Rock Paper Scissors",
                 font=("Arial", 22, "bold"),
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=20)

frame_display = tk.Frame(root, bg="#0f172a")
frame_display.pack(pady=20)

user_display = tk.Label(frame_display, text="", bg="#0f172a", fg="#22c55e")
user_display.grid(row=0, column=0, padx=40)

vs_label = tk.Label(frame_display, text="VS",
                    font=("Arial", 16, "bold"),
                    bg="#0f172a", fg="white")
vs_label.grid(row=0, column=1)

comp_display = tk.Label(frame_display, text="", bg="#0f172a", fg="#ef4444")
comp_display.grid(row=0, column=2, padx=40)

frame_buttons = tk.Frame(root, bg="#0f172a")
frame_buttons.pack(pady=20)

rock_btn = tk.Button(frame_buttons, text="🪨",
                     font=("Arial", 25),
                     width=4, height=2,
                     bg="#f97316", fg="white",
                     command=lambda: play("🪨"))
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(frame_buttons, text="📄",
                      font=("Arial", 25),
                      width=4, height=2,
                      bg="#3b82f6", fg="white",
                      command=lambda: play("📄"))
paper_btn.grid(row=0, column=1, padx=15)

scissors_btn = tk.Button(frame_buttons, text="✂",
                         font=("Arial", 25),
                         width=4, height=2,
                         bg="#10b981", fg="black",
                         command=lambda: play("✂"))
scissors_btn.grid(row=0, column=2, padx=15)

result_label = tk.Label(root, text="",
                        font=("Arial", 18, "bold"),
                        bg="#0f172a", fg="#eab308")
result_label.pack(pady=20)

score_label = tk.Label(root, text="You: 0   Computer: 0",
                       font=("Arial", 14),
                       bg="#0f172a", fg="#cbd5f5")
score_label.pack(pady=10)

reset_btn = tk.Button(root, text="🔄 Play Again",
                      font=("Arial", 12, "bold"),
                      bg="#ef4444", fg="white",
                      command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()