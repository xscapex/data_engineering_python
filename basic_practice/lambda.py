# edit_story

def edit_story(words, func):
    for word in words:
        print(func(word))

# Original method

def enliven(word):
    return word.capitalize() + '!'


# Lambda method

if __name__ == "__main__":

    stairs = ['a', 'b', 'c', 'd']

    print("Method 1: \n")
    edit_story(stairs, enliven)
    print("Method 2: \n")
    edit_story(stairs, lambda word : word.capitalize() + '!')