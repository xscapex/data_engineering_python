def balance_count(lst):
    # Step 1: Count how many times each integer appears in the list
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Step 2: Determine the maximum count value
    max_count = max(counts.values())
    
    # Step 3: Construct the result dictionary
    result = {k: max_count - v for k, v in counts.items() if max_count - v > 0}
    
    return result



if __name__ == "__main__":

    # lst = [1, 1, 2]
    lst = [1, 1, 1, 5, 3, 2, 2]
    # result = word_count_v2(lst)
    # print(max(result.values()))
    result = balance_count(lst)
    print(result)