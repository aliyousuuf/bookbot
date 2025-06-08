from stats import count_words

def get_book_text(book_path):

    with open(book_path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    #print(get_book_text("books/frankenstein.txt"))
    print(count_words("books/frankenstein.txt"))

if __name__ == "__main__":
    main() 

