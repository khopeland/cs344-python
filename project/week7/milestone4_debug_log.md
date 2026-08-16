# Course Project Milestone 4 Debugging Log

**Project:** Vocational Class Attendance Tracker  
**Student:** Kevin Copeland  
**Course:** CS344 Python  
**Milestone:** 4 – Debugging Log

## Bug 1 – Uppercase attendance input was rejected

**Description:**  
The program accepted lowercase `p` and `a` for present and absent, but uppercase `P` or `A` was treated as invalid input.

**Context:**  
This occurred in the individual attendance portion of the program when entering a member's attendance status. I noticed it while testing the same attendance entry with both lowercase and uppercase letters.

**Symptoms:**  
Entering `p` worked correctly, but entering `P` displayed the invalid-input message even though the user clearly meant present.

**Root Cause and Fix:**  
The condition only compared the input directly to lowercase strings. I fixed the issue by applying `.lower()` to the user's input before checking whether it was `p` or `a`.

**Debugging Technique:**  
I used small test cases and printed the value of the attendance variable before the condition. This showed that the input was being stored correctly but the comparison was case-sensitive. Testing `p`, `P`, `a`, and `A` made the problem easy to isolate and confirm after the fix.

---

## Bug 2 – Invalid class name caused the program to continue incorrectly

**Description:**  
When a user entered a class name that was not in the available class list, the program did not always stop or ask for a valid class before continuing.

**Context:**  
This happened while testing the overall class attendance option with an invalid class such as `Business Admin` when the program was expecting one of the class names stored in the current data structure.

**Symptoms:**  
The program either displayed incomplete results or attempted to continue without valid attendance data for the class.

**Root Cause and Fix:**  
The class validation condition was placed too late in the logic. I moved the validation check so the program verifies the class name before trying to access or calculate attendance information. Invalid class names now produce a clear message instead of continuing.

**Debugging Technique:**  
I isolated the class-selection section and tested it separately with valid and invalid names. By temporarily adding print statements showing the class entered and whether it existed in the class collection, I could see exactly where the program was continuing when it should have stopped.

---

## Bug 3 – Overall attendance totals were calculated incorrectly

**Description:**  
The overall class report produced incorrect present and absent totals during one of my tests.

**Context:**  
The problem appeared in the function that summarizes attendance for an entire class. I noticed it while testing a class with known values, such as 18 present and 2 absent.

**Symptoms:**  
The total displayed by the program did not match the attendance records I had entered. In some cases, the present total increased correctly while the absent total did not.

**Root Cause and Fix:**  
The counting logic used the wrong variable in one branch of the condition, causing one category to be counted incorrectly. I corrected the variable used in the absent branch and confirmed that present and absent totals were updated independently.

**Debugging Technique:**  
I printed the present and absent counters during each pass through the attendance records. Watching the counters change after each record showed exactly when the wrong total was being updated. I then ran a very small test set with only a few records to verify the corrected logic.

---

## Bug 4 – Yes/no prompt did not accept shortened responses consistently

**Description:**  
A prompt intended to accept `yes`, `y`, `no`, or `n` did not handle all four responses correctly.

**Context:**  
This appeared when the program asked whether the user wanted to perform another attendance action or continue using the program.

**Symptoms:**  
Typing `yes` worked, but a shortened response such as `y` could sometimes fall into the invalid-response branch. Similar behavior occurred with `n`.

**Root Cause and Fix:**  
The Boolean condition was written incorrectly and did not compare the variable separately against every accepted response. I rewrote the condition using membership checks such as `response in ("yes", "y")` and `response in ("no", "n")`, after converting the input to lowercase.

**Debugging Technique:**  
I traced the condition by hand and tested each expected response one at a time. This made it clear that the problem was not with `input()` but with the condition itself. Testing all four accepted values after the change confirmed that each followed the correct branch.

---

## Bug 5 – Member name lookup failed because of capitalization differences

**Description:**  
The individual attendance search could fail when the same member name was entered with different capitalization.

**Context:**  
This occurred in the individual attendance option when looking up a member before recording or displaying attendance.

**Symptoms:**  
A stored name such as `Kevin C` could be found when typed exactly the same way, but an entry such as `kevin c` could be reported as not found.

**Root Cause and Fix:**  
The member lookup compared the raw user input directly with the stored name. I fixed the issue by normalizing both values with `.lower()` during the comparison while keeping the original capitalization for display.

**Debugging Technique:**  
I printed both the entered name and the stored name during the lookup. The text looked the same to a person, but the printout and comparison showed that capitalization was causing the mismatch. I tested several capitalization combinations to make sure the lookup worked consistently after the fix.

---

## Reflection and Patterns

Two patterns appeared repeatedly while debugging this project. First, several bugs were caused by **user input not being normalized or validated early enough**. Capitalization differences and shortened responses could cause valid user intentions to be treated as errors. Second, some problems came from **conditional logic and variable handling**, especially when the program had multiple branches for present/absent totals or yes/no decisions.

In future programming work, I plan to take three specific actions. First, I will normalize user input with methods such as `.strip()` and `.lower()` before validating it. Second, I will test each function with small, predictable test cases before combining it with the rest of the program. Third, I will write and test conditions in smaller pieces so it is easier to see which branch is being executed and which variables are changing.

This milestone showed me that debugging is easier when I develop incrementally instead of waiting until the whole program is finished. Printing intermediate values, isolating sections of code, and testing one input at a time helped me move from seeing a symptom to identifying the actual cause of the problem.
