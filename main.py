def open_book(filename):
    with open(filename) as f:
        return f.read()

def word_count(book):
    return len(book.split())

def letter_count(book):
    letters = {}
    lowercase_book = book.lower()
    for letter in lowercase_book:
        if letter not in letters:
            letters[letter] = 0

        letters[letter] += 1

    return letters

def print_report(book):
    print("--- Begin report of books/frankenstein.text ---")
    print(f"Word count: {word_count(book)}")
    letters = letter_count(book)

    letters_list = list(letters.items())
    letters_list.sort(key=lambda x: x[1], reverse=True)

    for (letter, count) in letters_list:
        if letter.isalpha():
            print(f"The '{letter}' character appears {count} times.")

    print("--- End report ---")


print("hello world")

book = open_book("frankenstein.txt")
print_report(book)

