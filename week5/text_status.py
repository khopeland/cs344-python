def analyze_text(text):
    character_count = len(text)
    # Checked empty input to ensure the word count returns 0.
    word_count = len(text.split())
    e_count = text.count("e")

    return {
        "characters": character_count,
        "words": word_count,
        "lowercase_e": e_count
    }


def main():
    text = input("Enter a line of text: ")

    statistics = analyze_text(text)

    print("\nText Statistics")
    print("----------------")
    print("Characters including spaces:", statistics["characters"])
    print("Words:", statistics["words"])
    print('Lowercase "e" count:', statistics["lowercase_e"])


if __name__ == "__main__":
    main()