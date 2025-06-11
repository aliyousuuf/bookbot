def count_words(book):

    with open(book)  as f:
        words = f.read().split()
    return str(len(words))+" words found in the document"


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