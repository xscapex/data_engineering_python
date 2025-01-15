# Balance a List of Integers
# Given a list of ints, balance the list so that each int appears equally in the list. Return a dictionary where the key is the int and the value is the count needed to balance the list.
# [1, 1, 2] => {2: 1}

# [1, 1, 1, 5, 3, 2, 2] => {5: 2, 3: 2, 2: 1}


def word_count_v2(lst):
    words = lst
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

def balance_count(lst):

    word_dict = word_count_v2(lst)
    max_num = max(word_dict.values())
    result_dict = {}
    for key in word_dict.keys():
         dif = max_num - word_dict.get(key)
         if  dif > 0:
             result_dict[key] = dif
    return result_dict


if __name__ == "__main__":

    # lst = [1, 1, 2]
    lst = [1, 1, 1, 5, 3, 2, 2]
    # result = word_count_v2(lst)
    # print(max(result.values()))
    result = balance_count(lst)
    print(result)