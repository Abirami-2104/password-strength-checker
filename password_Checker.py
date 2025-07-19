#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 18:34:04 2025

@author: admin
"""

import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length at least 8
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Rule 2: Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append(" Add at least one UPPERCASE letter.")

    # Rule 3: Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Rule 4: Digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    # Rule 5: Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$...).")

    return score, feedback


def evaluate_password():
    print("Password Strength Checker \n")
    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)

    print(f"\nScore: {score}/5")

    if score <= 2:
        print("Weak password.")
    elif score == 3 or score == 4:
        print("⚠️ Medium strength password.")
    else:
        print("Strong password!")

    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(tip)


if __name__ == "__main__":
    evaluate_password()
