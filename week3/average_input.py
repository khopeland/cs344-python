# Week 3: Average from User-Entered Values

total = 0.0
number_count = 0

while True:
    user_entry = input("Enter a number or q to finish: ").strip()

    if user_entry.lower() == "q":
        break

    try:
        number = float(user_entry)
        total += number
        number_count += 1
    except ValueError:
        print("Invalid entry. Please enter a number or q.")

if number_count > 0:
    average = total / number_count
    print("Numbers entered:", number_count)
    print("Total:", total)
    print("Average:", average)
else:
    print("No valid numbers were entered, so an average cannot be computed.")

