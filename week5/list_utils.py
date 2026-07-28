def filter_and_summarize(numbers):
    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)

    count = len(positive_numbers)
    total = sum(positive_numbers)

    if count > 0:
        average = total / count
    else:
        average = 0

    return {
        "positive_numbers": positive_numbers,
        "count": count,
        "sum": total,
        "average": average
    }


def main():
    numbers = [12, -4, 0, 7, -9, 3, 15]

    summary = filter_and_summarize(numbers)

    print("Original list:", numbers)
    print("Positive numbers:", summary["positive_numbers"])
    print("Count:", summary["count"])
    print("Sum:", summary["sum"])
    print("Average:", summary["average"])


if __name__ == "__main__":
    main()