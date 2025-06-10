from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    file_content = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_content)
    print(f"{num_words} words found in the document")

main()