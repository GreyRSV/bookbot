def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        text = file.read()
    return text


def get_count_words(path: str = 'books/frankenstein.txt') -> int:
    words = get_book_text(path).split()
    return len(words)
