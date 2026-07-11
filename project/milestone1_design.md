# Course Project Milestone 1 Design

## Project Title

Vocational Attendance and Participation Tracker

## Problem Description

The Vocational Attendance and Participation Tracker will be a Python program designed to help vocational staff record and review attendance for members participating in vocational classes. The program will allow the user to enter a member's name, enter the vocational class, and record whether the member was present or absent. Classes may include HVAC, electrical, painting, culinary, GED, peer support, and other vocational programs.

The intended users are vocational instructors, supervisors, and managers who need a simple way to track class participation. In my work, attendance is important because it helps staff identify whether members are consistently participating, missing classes, or may need additional support before graduating from a vocational program.

The program will be useful because it will help vocational staff organize attendance records and calculate totals automatically instead of counting everything by hand. It will provide a clear summary showing how many members were present, how many were absent, and the overall attendance percentage. The program will use decisions to validate entries and respond to menu choices, while loops will allow staff to enter and review multiple attendance records.

The first version of the program will only store information while the program is running. It will not connect to New Freedom's systems, an online database, or a member record system. Member names and class names will be entered as text, and attendance will be recorded as present or absent. The program will assume that the amount of information entered is small enough to be stored in memory.

## Inputs and Outputs

### Inputs

The program will receive the following information from the user:

- Member name
- Vocational class name
- Attendance status, such as present or absent
- Menu selections
- A choice to add another record, view records, display a summary, or quit

### Outputs

The program will produce the following information:

- Confirmation that an attendance record was added
- A list of entered attendance records
- Total number of attendance records
- Number of present records
- Number of absent records
- Overall attendance percentage
- Messages for invalid menu choices or attendance entries
- A warning when a member has multiple absences

### Example Input and Output

Example input:

```text
Enter member name: Marcus Johnson
Enter vocational class: HVAC
Enter attendance status (present or absent): present
```

Desired output:

```text
Attendance record added successfully.

Member: Marcus Johnson
Vocational class: HVAC
Attendance status: Present
```

Example summary output:

```text
Vocational Attendance Summary
Total records: 5
Present: 4
Absent: 1
Attendance percentage: 80.0%
```

## Algorithm Overview

1. **Display the main menu.**  
   The program will show options for adding an attendance record, viewing all records, displaying an attendance summary, or quitting the program.

2. **Ask the user to select a menu option.**  
   The program will receive the user's choice and use a decision structure to determine which action to perform.

3. **Collect member attendance information.**  
   When the user chooses to add a record, the program will ask for the member's name, vocational class, and attendance status.

4. **Validate the attendance status.**  
   The program will use a decision to check whether the attendance status is present or absent. If the entry is invalid, a loop will ask the user to enter it again.

5. **Store the attendance record.**  
   The program will store the member name, vocational class, and attendance status together so the information can be reviewed later.

6. **Display saved attendance records.**  
   The program will use a loop to process and display each record that has been entered.

7. **Calculate attendance totals.**  
   The program will loop through the records and count the number of present and absent entries.

8. **Calculate the attendance percentage.**  
   The program will divide the number of present records by the total number of records and convert the result into a percentage.

9. **Display an attendance summary.**  
   The program will show the total records, present records, absent records, and overall attendance percentage.

10. **Repeat until the user chooses to quit.**  
    A loop will continue displaying the menu and accepting choices until the user selects the quit option.

### Decisions

The program will use decisions to:

- Determine which menu option the user selected
- Check whether an attendance entry is present or absent
- Detect invalid information
- Determine whether attendance records have been entered
- Avoid dividing by zero when there are no records
- Identify members who have multiple absences

### Loops

The program will use loops to:

- Keep the program running until the user chooses to quit
- Ask again when the user enters invalid information
- Process each saved attendance record
- Count present and absent records
- Display all attendance records

## Planned Structure and Functions

### `display_menu()`

This function will display the main menu choices for the vocational attendance program. It will not require any parameters and will print the available options.

### `get_menu_choice()`

This function will ask the user to select a menu option. It may not require any parameters and will return the user's menu choice.

### `get_attendance_record()`

This function will collect the member's name, vocational class, and attendance status. It will not require initial parameters and will return a completed attendance record.

### `validate_attendance_status(status)`

This function will check whether the user entered present or absent. It will receive the attendance status as a parameter and return `True` if it is valid or `False` if it is invalid.

### `display_records(records)`

This function will display all attendance records in a readable format. It will receive the list of records as a parameter and print each member's information.

### `calculate_attendance_summary(records)`

This function will calculate the total number of records, present records, absent records, and attendance percentage. It will receive the attendance records as a parameter and return the calculated summary information.

### `display_attendance_summary(records)`

This function will present the calculated attendance information to the user. It will receive the attendance records as a parameter and print a clearly labeled summary.