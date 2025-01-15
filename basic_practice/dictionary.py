# # 用 {} or dict() 來建立


from try_except import list_dict

if __name__ == '__main__':
    # 確保在主程式中運行
    # a_list = ['data', 'engineering', 'test']
    a_list = [['data', 1], ['engineering', 2]]

    print(list_dict(a_list))


# {'data': 1, 'engineering': 2}
    



# 用key來改 value
    
a_dict = {'data': 1, 'engineering': 2}
a_dict['data'] = 2

print(a_dict)

# 如何改 key?

## Method 1 

# a_dict['engineering1'] = a_dict.pop('engineering')

# print(a_dict)

## method 2 
a_dict['engineering1'] = a_dict.get('engineering')

del a_dict['engineering']

print(a_dict)


# update 若字典重複第二個將勝出

b_dict = {'data': 1}

a_dict.update(b_dict)

print(a_dict)



# clear() 來刪除所有項目

# keys() 取得所有 key

# values() 取得所有 value

# items() 取得所有的值對
print(a_dict.keys())
print(a_dict.values())
print(a_dict.items())

print(type(a_dict.keys()))
print(type(a_dict.values()))
print(type(a_dict.items()))