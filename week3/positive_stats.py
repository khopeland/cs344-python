# Week 3: Sum and Count of Positive Numbers

numbers = [12, -4, 7, 0, 15, -8, 3, 9, -2, 5]

positive_count = 0
positive_sum = 0

# Loop through the list and accumulate the count and sum of positive numbers.
for number in numbers:
    if number > 0:
        positive_count += 1
        positive_sum += number

print("Number list:", numbers)
print("Count of positive numbers:", positive_count)
print("Sum of positive numbers:", positive_sum)