"""Week 6 Mini-App: Grade Report Analyzer

Reads student names and scores from a text file, calculates class statistics,
and prints a clear summary report.

Expected file format:
student name,score

Example:
Kevin Copeland,92
Dominic Smith,85
"""

from pathlib import Path


def process_grade_file(file_name):
    """Read and analyze a grade file.

    Returns:
        tuple: (student_records, skipped_count)
    """
    student_records = []
    skipped_count = 0

    try:
        with open(file_name, "r", encoding="utf-8") as grade_file:
            for line_number, line in enumerate(grade_file, start=1):
                line = line.strip()

                # Skip empty lines to avoid parsing and index errors.
                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 2:
                    print(
                        f"Warning: Line {line_number} was skipped "
                        "because it does not contain a student name and score."
                    )
                    skipped_count += 1
                    continue

                student_name = parts[0].strip()
                score_text = parts[1].strip()

                if not student_name:
                    print(
                        f"Warning: Line {line_number} was skipped "
                        "because the student name is missing."
                    )
                    skipped_count += 1
                    continue

                try:
                    score = float(score_text)
                except ValueError:
                    print(
                        f"Warning: Line {line_number} was skipped "
                        f"because '{score_text}' is not a valid score."
                    )
                    skipped_count += 1
                    continue

                if score < 0 or score > 100:
                    print(
                        f"Warning: Line {line_number} was skipped "
                        "because the score must be between 0 and 100."
                    )
                    skipped_count += 1
                    continue

                student_records.append(
                    {
                        "name": student_name,
                        "score": score,
                    }
                )

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found.")
        return None
    except OSError as error:
        print(f"Error: The file could not be read: {error}")
        return None

    return student_records, skipped_count


def print_report(file_name, student_records, skipped_count):
    """Calculate and print the grade summary report."""
    print("\n" + "=" * 48)
    print("GRADE REPORT ANALYZER")
    print("=" * 48)
    print(f"Input file: {Path(file_name).name}")
    print(f"Students processed: {len(student_records)}")
    print(f"Malformed records skipped: {skipped_count}")
    print("-" * 48)

    if not student_records:
        print("No valid student records were found.")
        print("=" * 48)
        return

    total_score = sum(record["score"] for record in student_records)
    average_score = total_score / len(student_records)

    highest_student = max(
        student_records,
        key=lambda record: record["score"]
    )

    lowest_student = min(
        student_records,
        key=lambda record: record["score"]
    )

    print(f"Class average: {average_score:.2f}")
    print(
        f"Highest grade: {highest_student['name']} - "
        f"{highest_student['score']:.2f}"
    )
    print(
        f"Lowest grade:  {lowest_student['name']} - "
        f"{lowest_student['score']:.2f}"
    )

    print("-" * 48)
    print("Student grades:")

    for record in sorted(
        student_records,
        key=lambda item: item["name"].lower()
    ):
        print(
            f"  {record['name']:<28} "
            f"{record['score']:>6.2f}"
        )

    print("=" * 48)


def main():
    """Ask for a file name, process it, and display the report."""
    script_folder = Path(__file__).parent
    default_file_name = "grades_small.txt"

    print("Week 6 Grade Report Analyzer")

    file_choice = input(
        f"Enter the grade file name [{default_file_name}]: "
    ).strip()

    if not file_choice:
        file_choice = default_file_name

    # Build a path to the selected file inside the week6 folder.
    file_name = script_folder / file_choice

    results = process_grade_file(file_name)

    if results is not None:
        student_records, skipped_count = results
        print_report(
            file_name,
            student_records,
            skipped_count
        )


if __name__ == "__main__":
    main()