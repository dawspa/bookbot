def count_words(book_content):
    words_list = book_content.split()
    words_num = len(words_list)
    print(f"----------- Word Count ----------\nFound {words_num} total words")

def count_characters(book_content):
    non_capitalized = book_content.lower()
    chars_dict = {}
    for char in non_capitalized:
        chars_dict[char] = chars_dict.get(char, 0) + 1
    return chars_dict

def sort_chars_dict(dict):
    return dict["num"]

def split_dict_into_list(book_content):
    splitted_dicts = [{"char": k, "num": v} for k,v in count_characters(book_content).items()]
    splitted_dicts.sort(reverse=True, key=sort_chars_dict)
    return splitted_dicts

def print_char_count(book_content):
    print("--------- Character Count -------")
    for char_dict in split_dict_into_list(book_content):
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")