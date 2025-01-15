# 用 () or tuple() 來建立

# unpacking

marx_tuple = ('a', 'b', 'c', 'd')

a, b, c, d = marx_tuple

print(a, b, c, d)


# tuple() 來轉換成 tuple

a_list = ['data', 'engineering', 'test']
tuple_test = tuple(a_list)
list_test = list(tuple_test)
print(tuple_test)
print(list_test)