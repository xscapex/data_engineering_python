# Given a sentence, count the distinct words in the sentence

def word_count(sentence):
    return len(set(sentence.split()))



if __name__ == '__main__':
    result = word_count("Data Engineering test")
    print(result)