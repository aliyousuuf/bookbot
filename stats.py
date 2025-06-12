def get_book_text(book_path):

    with open(book_path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(book):

    with open(book)  as f:
        words = f.read().split()
    return str(len(words))


def character_count(book_path):

    char_count = dict()

    with open(book_path) as file:
        for line in file:
            #print(line)

            for character in line:
                character = character.lower()
                #print(character.lower())

                if character in char_count:
                    char_count[character] = char_count[character] + 1
                else:
                    char_count[character] = 1
    return char_count

def sorting_chars_dict(count_char_dict):

    sorted_dict = dict(sorted(count_char_dict.items(), reverse=True, key=lambda item: item[1]))
    return sorted_dict

def print_output(path_to_book):

    total_words = count_words(path_to_book)
    
    char_count = character_count(path_to_book)
    #print(char_count)


    characters_count_sorted = sorting_chars_dict(char_count)
    #print(characters_count_sorted)

    #
    # del characters_count_sorted[" "]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(total_words) + " total words")
    print("--------- Character Count -------")

    for char, count in characters_count_sorted.items():
        print(char + ": " + str(count))


