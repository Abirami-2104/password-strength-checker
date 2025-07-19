#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 18:39:09 2025

@author: admin
"""

import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one UPPERCASE letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$...).")

    return score, feedback


def on_check():
    password = entry.get()
    score, feedback = check_password_strength(password)

    # Update label
    score_label.config(text=f"Score: {score}/5")

    if score <= 2:
        strength_label.config(text="Weak", fg="red")
    elif score <= 4:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

    # Update suggestion box
    feedback_box.delete('1.0', tk.END)
    if feedback:
        for line in feedback:
            feedback_box.insert(tk.END, f"{line}\n")
    else:
        feedback_box.insert(tk.END, "Great password! ")


# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter Password:", font=("Helvetica", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, show="*", font=("Helvetica", 12))
entry.pack()

tk.Button(root, text="Check Password", command=on_check, font=("Helvetica", 12)).pack(pady=10)

score_label = tk.Label(root, text="Score: ", font=("Helvetica", 12))
score_label.pack()

strength_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
strength_label.pack(pady=5)

tk.Label(root, text="Suggestions:", font=("Helvetica", 11)).pack()
feedback_box = tk.Text(root, height=6, width=45)
feedback_box.pack(pady=5)

root.mainloop()
