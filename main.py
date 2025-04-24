import sys
import os

from stats import get_num_words
from stats import get_freq_dict
from stats import sort_freq_dict

def get_book_text(path_to_file):
    """Reads the content of the book from the file."""

    file_contents = ""
    
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def parse_argv(argv):
    """Parses and validates the file path from the command-line arguments."""

    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = argv[1]

    if not os.path.isfile(file_path):
        print(f"Error: File {file_path} does not exist.")
        sys.exit(1)

    return file_path    

def main():
    path_to_book = parse_argv(sys.argv)
 
    file_content = get_book_text(path_to_book)
    num_words = get_num_words(file_content)
    freq_dict = get_freq_dict(file_content)
    sorted_freq_dict = sort_freq_dict(freq_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in sorted_freq_dict:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

    