def is_Palindrome(string):
    string_list = list(string)
    # string_list_r = string_list.reverse()
    print('string_list: ',string_list)
    # print('string_list_r: ',string_list_r)
    print('string_list reverse: ',string_list[::-1])
    if string_list == string_list[::-1]:
        return True
    else:
        return False
    

def is_Palindrome(x: int) -> bool:
    # Convert the integer to a string
    str_x = str(x)
    # Compare the string with its reverse
    return str_x == str_x[::-1]

if __name__ == '__main__':
    string = 'abba'
    result = is_Palindrome(string)
    print(result)

