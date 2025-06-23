from collections import Counter


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        text = file.read()
    return text


def get_count_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_count_chars(text: str) -> dict[str, int]:
    letters = Counter(text.lower())
    return letters
