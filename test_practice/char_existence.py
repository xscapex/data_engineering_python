# For a given word and character, does the character exist in the word.


def char_existence(word, char):

    return char in word



if __name__ == "__main__":

    word = "This is the data engineering test"
    char = "Data"
    result = char_existence(word, char)
    print(result)