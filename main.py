from stats import get_book_text, get_count_chars, get_count_words


def main():
    path: str = 'books/frankenstein.txt'
    text = get_book_text(path)
    count_words = get_count_words(text)
    count_chars = get_count_chars(text)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {count_words} total words')
    print('--------- Character Count -------')
    for char, number in count_chars.most_common():
        if char.isalpha():
            print(f'{char}: {number}')
    print('============= END ===============')


main()
