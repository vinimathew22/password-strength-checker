import tkinter as tk
from tkinter import ttk
import re

def check_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Lowercase letter(s)")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Uppercase letter(s)")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Digit(s)")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Special character(s)")
    
    if score == 5:
        strength = "Very Strong"
        color = "dark green"
    elif score == 4:
        strength = "Strong"
        color = "green"
    elif score == 3:
        strength = "Medium"
        color = "orange"
    elif score == 2:
        strength = "Weak"
        color = "red"
    else:
        strength = "Very Weak"
        color = "dark red"
    
    if feedback:
        feedback_str = "Improve by adding: " + ", ".join(feedback)
    else:
        feedback_str = "Excellent password!"
    
    return strength, feedback_str, color, score

def update_strength(*args):
    password = entry.get()
    if password:
        strength, feedback, color, score = check_strength(password)
        label_strength.config(text=strength, foreground=color)
        label_feedback.config(text=feedback)
        progress['value'] = score * 20  
    else:
        label_strength.config(text="")
        label_feedback.config(text="")
        progress['value'] = 0

#main
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x350")
root.resizable(False, False)
root.configure(padx=20, pady=20)

ttk.Label(root, text="Password Strength Checker", font=("Helvetica", 18, "bold")).pack(pady=(0, 20))

ttk.Label(root, text="Enter password:", font=("Helvetica", 12)).pack(anchor="w")
entry = ttk.Entry(root, show="*", font=("Helvetica", 14), width=35)
entry.pack(pady=(5, 20))
entry.bind("<KeyRelease>", update_strength)

label_strength = ttk.Label(root, text="", font=("Helvetica", 20, "bold"))
label_strength.pack(pady=(0, 10))

label_feedback = ttk.Label(root, text="", font=("Helvetica", 11), foreground="gray", wraplength=400)
label_feedback.pack(pady=(0, 20))

style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=20)
progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", style="TProgressbar")
progress.pack()

update_strength()

root.mainloop()