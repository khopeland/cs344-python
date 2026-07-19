# Course Project Milestone 2 Status

## Project Title

Vocational Attendance Tracker

## Features Implemented

For Milestone 2, I created a working version of the Vocational Attendance Tracker.

The program allows the user to choose between two attendance tracking methods:

1. Individual member attendance
2. Overall class attendance

The individual attendance option allows the user to enter each member's name, vocational class, and attendance status. The program accepts present, p, absent, or a for faster data entry. It then counts the total present and absent records and calculates the attendance percentage.

The overall class attendance option allows the user to enter a vocational class, the total number of members present, and the total number absent. The user can also choose whether to include the names of the absent members. The program can record multiple vocational classes and provides both individual class summaries and a combined attendance summary.

The program uses functions to separate the major tasks, including validating input, collecting records, processing attendance totals, and displaying results.

## Features Planned for Later Milestones

In future milestones, I plan to add or improve the following features:

- Add the date for each attendance entry.
- Add a main menu that allows the user to select additional actions.
- Save attendance records to a file.
- Allow saved attendance records to be viewed later.
- Add summaries by vocational class or member.
- Improve validation for member names and class names.
- Allow the user to return to the main menu without restarting the program.

## Issues or Questions

One issue I encountered was making sure the loops ended correctly and did not create an infinite loop. I used validation loops that continue only until the user enters an accepted response.

I also added abbreviated responses such as y, n, p, and a to make attendance entry faster. These responses are converted into complete values before the records are processed.

The current version stores attendance records only while the program is running. Saving the information permanently will be added in a later milestone.