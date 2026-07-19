# Week 3: Character Counter

text = input("Enter a line of text: ")
search_character = input("Enter one character to search for: ")

while len(search_character) != 1:
    print("Please enter exactly one character.")
    search_character = input("Enter one character to search for: ")

character_count = 0

# Traverse the text one character at a time and count matching characters.
for character in text:
    if character == search_character:
        character_count += 1

print(
    f"The character '{search_character}' was found "
    f"{character_count} time(s) in the text."
)