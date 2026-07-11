# This program converts a numeric score into a letter grade.

score = int(input("Enter a numeric score between 0 and 100: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a whole number between 0 and 100.")
elif score >= 90:
    letter_grade = "A"
elif score >= 80:
    letter_grade = "B"
elif score >= 70:
    letter_grade = "C"
elif score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

if 0 <= score <= 100:
    print(f"Score: {score} -> Letter grade: {letter_grade}")