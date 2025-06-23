"""Программа bookbot считает количество слов и символов в переданном файле."""
from stats import get_book_text, get_count_chars, get_count_words, print_report


def main():
    """Стартовая точка программы."""
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    count_words = get_count_words(text)
    count_chars = get_count_chars(text)
    print_report(path, count_words, count_chars)


main()
