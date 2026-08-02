# Milestone 3 Test Plan

## Overview and Scope

This test plan evaluates the currently implemented features of the Vocational Attendance Tracker project. Testing focuses on both individual member attendance and overall class attendance.

The features being tested include:

- Selecting an attendance entry mode
- Entering individual member attendance records
- Entering overall class attendance records
- Recording present and absent attendance
- Entering multiple records during one program session
- Validating yes/no responses
- Calculating attendance totals
- Calculating attendance percentages
- Displaying individual and overall attendance summaries

## Test Environment

- Operating system: Windows 11 Pro
- Python version: Python 3
- Development environment: Visual Studio Code
- Program tested: `project_main.py`
- Test location: Local computer
- Repository: `cs344-python`

## Test Cases

| Test # | Description | Input Values | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1 | Select overall class attendance mode | Enter `2` at the main menu | Program opens the Overall Class Attendance section | The Overall Class Attendance section opened correctly | Pass |
| 2 | Record Peer Support class attendance | Class: Peer Support, Present: `18`, Absent: `2` | Program calculates 20 total members and 90.0% attendance | Program displayed 20 total members, 18 present, 2 absent, and 90.0% attendance | Pass |
| 3 | Record another class in the same session | Enter `y`, then Class: HVAC, Present: `19`, Absent: `1` | Program accepts another class and calculates 95.0% attendance | HVAC was recorded with 20 total members and 95.0% attendance | Pass |
| 4 | Record a class with a different total size | Class: Framing, Present: `17`, Absent: `1` | Program calculates 18 total members and 94.4% attendance | Program displayed 18 total members and 94.4% attendance | Pass |
| 5 | Reject an invalid yes/no response | Enter `Business Admin` when asked whether to log another class | Program rejects the input and asks the question again | Program displayed an invalid-choice message and repeated the prompt | Pass |
| 6 | Accept valid input after an invalid response | Enter `y` after the invalid response | Program continues to the next class entry | Program continued and allowed another class to be entered | Pass |
| 7 | Handle a class with zero absent members | Class: Business Admin, Present: `14`, Absent: `0` | Program calculates 100.0% attendance without crashing | Program displayed 14 total members and 100.0% attendance | Pass |
| 8 | Stop overall class entry | Enter `n` when asked whether to log another class | Program stops collecting class records and displays the summaries | Program displayed all class summaries and the combined summary | Pass |
| 9 | Calculate combined attendance totals | Four classes with 72 total records, 68 present, and 4 absent | Program displays the correct combined totals | Program displayed 4 classes, 72 total records, 68 present, and 4 absent | Pass |
| 10 | Calculate combined attendance percentage | 68 present out of 72 total attendance records | Program calculates 94.4% overall attendance | Program displayed 94.4% overall attendance | Pass |
| 11 | Select individual member attendance mode | Enter `1` at the main menu | Program opens the Individual Member Attendance section | The Individual Member Attendance section opened correctly | Pass |
| 12 | Record a present individual member | Name: Kevin C, Class: HVAC, Status: `p` | Program stores Kevin C as present in HVAC | Program displayed Kevin C in HVAC with status Present | Pass |
| 13 | Record another present member | Enter `y`, then Name: Dominic S, Class: Framing, Status: `p` | Program stores Dominic S as present in Framing | Program displayed Dominic S in Framing with status Present | Pass |
| 14 | Reject an invalid individual yes/no response | Enter `James` when asked whether to enter another member | Program rejects the input and asks the question again | Program displayed an invalid-choice message and repeated the prompt | Pass |
| 15 | Accept valid input after invalid individual response | Enter `y` after the invalid response | Program continues to another member entry | Program continued and allowed James to be entered | Pass |
| 16 | Record an absent individual member | Name: James, Class: Electrical, Status: `a` | Program stores James as absent in Electrical | Program displayed James in Electrical with status Absent | Pass |
| 17 | Stop individual member entry | Enter `n` after the third member | Program stops collecting member records and displays the summary | Program displayed all individual attendance records and the attendance summary | Pass |
| 18 | Calculate individual attendance totals | Three records with 2 present and 1 absent | Program displays 3 total records, 2 present, and 1 absent | Program displayed the correct totals | Pass |
| 19 | Calculate individual attendance percentage | 2 present out of 3 total records | Program calculates 66.7% attendance | Program displayed 66.7% attendance | Pass |

## Findings and Next Steps

### Findings

All completed test cases passed. The Vocational Attendance Tracker successfully handled both overall class attendance and individual member attendance.

The program correctly:

- Opened the selected attendance mode
- Recorded multiple classes during one session
- Recorded multiple individual members during one session
- Accepted present and absent attendance entries
- Calculated class attendance totals
- Calculated individual attendance totals
- Calculated attendance percentages
- Handled a class with zero absent members
- Rejected invalid yes/no responses
- Allowed the user to continue after entering an invalid yes/no response
- Displayed readable attendance summaries

No defects were discovered during the completed tests.

### Next Steps

Before the final project submission, additional testing should be completed for the following situations:

- An invalid main menu selection
- A non-numeric value entered for the number present or absent
- A negative number entered for attendance totals
- An invalid individual attendance status
- A class with zero present and zero absent members
- Entering the names of absent class members
- Empty member or class names

If any of these additional tests fail, the program will be updated and the fixes will be documented in the project status file.

### Features Not Yet Tested

The option to include the names of absent members has not yet been fully tested. Additional invalid numeric and empty-input situations have also not yet been tested.