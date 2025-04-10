from stats import get_num_words
from stats import get_freq_dict
from stats import sort_freq_dict

def get_book_text(path_to_file):
    file_contents = ""
    
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    path_to_book = "books/frankenstein.txt"
    
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
    
main()

    