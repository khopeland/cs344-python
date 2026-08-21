# CS 344 Course Project
# Final Project: Vocational Attendance Tracker


def get_yes_no(prompt):
    """Get a valid yes/y or no/n response from the user."""

    answer = input(prompt).strip().lower()

    while answer not in ["yes", "y", "no", "n"]:
        print("Invalid choice. Please enter yes, y, no, or n.")
        answer = input(prompt).strip().lower()

    return answer in ["yes", "y"]


def get_nonempty_text(prompt, field_name):
    """Get required text input and reject blank entries."""

    value = input(prompt).strip()

    while value == "":
        print(f"{field_name} cannot be blank.")
        value = input(prompt).strip()

    return value


def get_nonnegative_integer(prompt):
    """Get a whole number that is zero or greater."""

    while True:
        user_entry = input(prompt).strip()

        try:
            number = int(user_entry)

            if number >= 0:
                return number

            print("Please enter a number that is zero or greater.")

        except ValueError:
            print("Invalid entry. Please enter a whole number.")


def choose_tracking_method():
    """Ask the user how they want to track attendance."""

    print("How would you like to record attendance?")
    print("1. Individual member attendance")
    print("2. Overall class attendance")

    choice = input("Enter 1 or 2: ").strip()

    while choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter 1 or 2: ").strip()

    return choice


def get_individual_record():
    """Ask the user for one individual attendance record."""

    member_name = get_nonempty_text(
        "Enter the member's name: ", "Member name"
    )
    class_name = get_nonempty_text(
        "Enter the vocational class: ", "Vocational class"
    )

    attendance_status = input(
        "Enter attendance status (present/p or absent/a): "
    ).strip().lower()

    while attendance_status not in ["present", "p", "absent", "a"]:
        print("Invalid status. Please enter present, p, absent, or a.")
        attendance_status = input(
            "Enter attendance status (present/p or absent/a): "
        ).strip().lower()

    if attendance_status == "p":
        attendance_status = "present"
    elif attendance_status == "a":
        attendance_status = "absent"

    record = {
        "member_name": member_name,
        "class_name": class_name,
        "status": attendance_status
    }

    return record


def process_individual_records(records):
    """Count present and absent records and calculate attendance percentage."""

    present_count = 0
    absent_count = 0

    for record in records:
        if record["status"] == "present":
            present_count += 1
        else:
            absent_count += 1

    total_records = len(records)

    if total_records > 0:
        attendance_percentage = (present_count / total_records) * 100
    else:
        attendance_percentage = 0

    summary = {
        "total": total_records,
        "present": present_count,
        "absent": absent_count,
        "percentage": attendance_percentage
    }

    return summary


def display_individual_results(records, summary):
    """Display individual records and the attendance summary."""

    print("\nIndividual Attendance Records")
    print("-----------------------------")

    for record in records:
        print(
            f"Member: {record['member_name']} | "
            f"Class: {record['class_name']} | "
            f"Status: {record['status'].title()}"
        )

    print("\nAttendance Summary")
    print("------------------")
    print(f"Total records: {summary['total']}")
    print(f"Present: {summary['present']}")
    print(f"Absent: {summary['absent']}")
    print(f"Attendance percentage: {summary['percentage']:.1f}%")


def run_individual_tracking():
    """Record attendance one member at a time."""

    attendance_records = []

    print("\nIndividual Member Attendance")
    print("----------------------------")

    while True:
        record = get_individual_record()
        attendance_records.append(record)

        add_another = get_yes_no(
            "\nWould you like to enter another member? "
            "(yes/y or no/n): "
        )

        if not add_another:
            break

        print()

    summary = process_individual_records(attendance_records)
    display_individual_results(attendance_records, summary)


def get_absent_names(absent_count):
    """Collect the names of absent members."""

    absent_names = []

    print("\nEnter the names of the absent members.")

    for number in range(1, absent_count + 1):
        name = input(f"Absent member {number}: ").strip()

        while name == "":
            print("The member's name cannot be blank.")
            name = input(f"Absent member {number}: ").strip()

        absent_names.append(name)

    return absent_names


def get_overall_class_record():
    """Get overall attendance totals for one vocational class."""

    class_name = get_nonempty_text(
        "\nEnter the vocational class: ", "Vocational class"
    )

    present_count = get_nonnegative_integer(
        "Enter the total number of members present: "
    )

    absent_count = get_nonnegative_integer(
        "Enter the total number of members absent: "
    )

    absent_names = []

    if absent_count > 0:
        include_names = get_yes_no(
            "Would you like to include the names of absent members? "
            "(yes/y or no/n): "
        )

        if include_names:
            absent_names = get_absent_names(absent_count)

    total_members = present_count + absent_count

    if total_members > 0:
        attendance_percentage = (present_count / total_members) * 100
    else:
        attendance_percentage = 0

    class_record = {
        "class_name": class_name,
        "present": present_count,
        "absent": absent_count,
        "total": total_members,
        "percentage": attendance_percentage,
        "absent_names": absent_names
    }

    return class_record


def display_overall_results(class_records):
    """Display attendance summaries for all entered classes."""

    print("\nOverall Class Attendance Summary")
    print("--------------------------------")

    total_present = 0
    total_absent = 0

    for record in class_records:
        print(f"\nVocational class: {record['class_name']}")
        print(f"Total members: {record['total']}")
        print(f"Present: {record['present']}")
        print(f"Absent: {record['absent']}")
        print(f"Attendance percentage: {record['percentage']:.1f}%")

        if record["absent_names"]:
            print("Absent members:")

            for name in record["absent_names"]:
                print(f"- {name}")

        total_present += record["present"]
        total_absent += record["absent"]

    total_attendance = total_present + total_absent

    if total_attendance > 0:
        overall_percentage = (
            total_present / total_attendance
        ) * 100
    else:
        overall_percentage = 0

    print("\nCombined Attendance Summary")
    print("---------------------------")
    print(f"Classes recorded: {len(class_records)}")
    print(f"Total attendance records: {total_attendance}")
    print(f"Total present: {total_present}")
    print(f"Total absent: {total_absent}")
    print(f"Overall attendance percentage: {overall_percentage:.1f}%")


def run_overall_tracking():
    """Record overall attendance totals for one or more classes."""

    class_records = []

    print("\nOverall Class Attendance")
    print("------------------------")

    while True:
        class_record = get_overall_class_record()
        class_records.append(class_record)

        log_another = get_yes_no(
            "\nWould you like to log another vocational class? "
            "(yes/y or no/n): "
        )

        if not log_another:
            break

    display_overall_results(class_records)


def main():
    """Coordinate the overall attendance tracker program."""

    print("Vocational Attendance Tracker")
    print("-----------------------------")

    tracking_method = choose_tracking_method()

    if tracking_method == "1":
        run_individual_tracking()
    else:
        run_overall_tracking()


if __name__ == "__main__":
    main()