import sys 
from stats import *

#frankenstein_book = "books/frankenstein.txt"


def main():
    #print(get_book_text("books/frankenstein.txt"))
    #print(count_words("books/frankenstein.txt"))
    #print(character_count("books/frankenstein.txt"))

    if len(sys.argv) > 3 or len(sys.argv) <=1 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("analyzing book: " + sys.argv[1])
        print_output(sys.argv[1])
    


    #print_output(frankenstein_book)

if __name__ == "__main__":
    main() 

