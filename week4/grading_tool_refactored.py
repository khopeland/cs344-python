# grading_tool_refactored.py
# Week 4 - Refactoring a Python Script into Functions

# Planned functions:
# 1. get_score() - Gets and validates each score entered by the user.
# 2. calculate_average() - Calculates the average of the scores.
# 3. determine_letter_grade() - Determines the letter grade from the average.
# 4. display_results() - Displays the final grade report.


def get_score(assignment_name):
    """
    Ask the user to enter a score for an assignment.

    Input:
        assignment_name (str): The name of the assignment.

    Output:
        float: A validated score between 0 and 100.
    """
    while True:
        try:
            score = float(
                input(f"Enter the score for {assignment_name} (0-100): ")
            )

            if 0 <= score <= 100:
                return score

            print("Please enter a score between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a numerical score.")


def calculate_average(scores):
    """
    Calculate the average of a list of scores.

    Input:
        scores (list): A list containing numerical assignment scores.

    Output:
        float: The average of all scores in the list.
    """
    return sum(scores) / len(scores)


def determine_letter_grade(average):
    """
    Determine the letter grade for a numerical average.

    Input:
        average (float): The student's numerical grade average.

    Output:
        str: The corresponding letter grade.
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def display_results(student_name, scores, average, letter_grade):
    """
    Display the student's scores and final grade.

    Inputs:
        student_name (str): The student's name.
        scores (list): The student's assignment scores.
        average (float): The calculated grade average.
        letter_grade (str): The student's final letter grade.

    Output:
        None
    """
    print("\n--- Grade Summary ---")
    print(f"Student: {student_name}")

    for assignment_number, score in enumerate(scores, start=1):
        print(f"Assignment {assignment_number}: {score:.2f}")

    print(f"Average Score: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")


def main():
    """
    Coordinate the overall flow of the grading tool.

    Input:
        User-entered student name and assignment scores.

    Output:
        A complete grade summary displayed to the user.
    """
    print("Welcome to the Grading Tool")

    student_name = input("Enter the student's name: ").strip()

    while not student_name:
        print("The student's name cannot be blank.")
        student_name = input("Enter the student's name: ").strip()

    scores = []

    for assignment_number in range(1, 4):
        score = get_score(f"Assignment {assignment_number}")
        scores.append(score)

    average = calculate_average(scores)
    letter_grade = determine_letter_grade(average)

    display_results(student_name, scores, average, letter_grade)


if __name__ == "__main__":
    main()