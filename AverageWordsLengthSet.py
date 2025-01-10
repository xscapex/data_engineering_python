# input
# {'Data','Engineeering', 'test'}

# expected output

'(4+12+4)3 '


def average_word_length(sentence):

    # Since the input is a set of words, there’s no need to split anything.
    # words = sentence.split()
    words = sentence
    # print(words)
    # print(len(word) for word in words)
    total_length = sum(len(word) for word in words)
    return total_length/len(words)



if __name__ == "__main__":
    sentence = {'Data','Engineeering', 'test'}
    result = average_word_length(sentence)
    print(result)