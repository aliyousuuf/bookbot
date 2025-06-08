def count_words(book):

    with open(book)  as f:
        words = f.read().split()
    return str(len(words))+" words found in the document"