import sys

from stats import get_word_count
from stats import get_count_by_char
from stats import sort_count_by_char

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    num_words = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = sort_count_by_char(get_count_by_char(book_text))
    print("--------- Character Count -------")
    for count in char_counts:
        print(f"{count["char"]}: {count["num"]}")

main()