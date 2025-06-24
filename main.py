"""Программа bookbot считает количество слов и символов в переданном файле."""
import sys

from stats import get_book_text, get_count_chars, get_count_words, print_report


def main():
    """Стартовая точка программы."""
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    count_words = get_count_words(text)
    count_chars = get_count_chars(text)
    print_report(path, count_words, count_chars)


main()
