import sys
from stats import count_words, print_char_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    args = sys.argv

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        return f.read()
    
def main():
    print("============ BOOKBOT ============")
    file_content = get_book_text(args[1])
    count_words(file_content)
    print_char_count(file_content)
    print("============= END ===============")

main()