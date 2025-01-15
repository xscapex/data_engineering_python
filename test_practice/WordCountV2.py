
# Answer
def word_count_v2(sentence):
    words = sentence.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict, len(word_dict)

# Test
# {'Data':1, 'Engineering':1, 'test':2}

# def word_count_v2(sentence):
#     #words = sentence.split(',')
#     words = sentence.split()
#     print(words)
#     word_dict = {}
#     for word in words:
#         print(word_dict.get(word, 0))
#     # for word in words:
#     #     word_dict[word] = word_dict.get(word, 0) + 1
#     # return len(word_dict)

# # Small test1
# word_dict = {'Data':1}
# word = 'Data'
# word_dict[word] = word_dict.get(word, 0) + 1
# print(word_dict[word])

# Small test2
# word_dict.get(word) 還是需要寫 word_dict.get(word, 0) 否則會出現錯誤
# word_dict = {}
# word = 'Data'
# print(word_dict.get(word))
# word_dict[word] = word_dict.get(word) + 1
# print(word_dict[word])


if __name__ == '__main__':
    result = word_count_v2("Data Engineering, test test")
    print(result)
    # print(type("example".split))