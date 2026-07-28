def count_words(text):
    text = text.lower()
    words = text.split()

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def main():
    text = input("Enter a line or short paragraph: ")

    frequencies = count_words(text)

    print("\nWord Frequencies")
    print("----------------")

    if len(frequencies) == 0:
        print("No words were entered.")
    else:
        for word, count in frequencies.items():
            print(word, ":", count)


if __name__ == "__main__":
    main()