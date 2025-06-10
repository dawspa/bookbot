def count_words(book_content):
    words_list = book_content.split()
    return len(words_list)

def count_characters(book_content):
    non_capitalized = book_content.lower()
    chars_dict = {}
    for char in non_capitalized:
        chars_dict[char] = chars_dict.get(char, 0) + 1
    return chars_dict