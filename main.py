def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(book_content):
    words_list = book_content.split()
    return len(words_list)
    
def main():
    file_content = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_content)
    print(f"{num_words} words found in the document")
    
main()