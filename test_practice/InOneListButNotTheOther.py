#check for words that exists in two lists
arr1 = ["this", "is", "my", "test"]
arr2 = ["this", "is", "my", "array"]

def uniqueWords(arr1, arr2):
  result = {}
  for word in arr1:
    result[word]=1
  for word2 in arr2:
    if word2 in result:
      result[word2]=2
    else:
      result[word2]=1
  # return [w for w in result if result[w] == 1]
  return result


if __name__ == '__main__':
    arr1 = ["this", "is", "my", "test"]
    arr2 = ["this", "is", "my", "array"]
    result = uniqueWords(arr1, arr2)
    print(result)