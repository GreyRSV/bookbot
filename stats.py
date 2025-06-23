"""Вспомогательные функции программы."""
from collections import Counter


def get_book_text(path_to_file: str) -> str:
    """Получи текст из файла."""
    with open(path_to_file, encoding='utf-8') as file:
        text = file.read()
    return text


def get_count_words(text: str) -> int:
    """Посчитай количество слов в тексте."""
    words = text.split()
    return len(words)


def get_count_chars(text: str) -> Counter[str]:
    """Посчитай количество символов в тексте."""
    letters = Counter(text.lower())
    return letters


def print_report(
    path: str, count_words: int, count_chars: Counter[str]
) -> None:
    """Выведи отчёт о количестве слов и букв в файле."""
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {count_words} total words')
    print('--------- Character Count -------')
    for char, number in count_chars.most_common():
        if char.isalpha():
            print(f'{char}: {number}')
    print('============= END ===============')
