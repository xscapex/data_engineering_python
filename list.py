# 用 [] or list() 來建立

# 用 list () 來將其他的資料類型轉換成 list

print("Example 01: list('cat'): ", list('cat'))

a_tuple = ('ready', 'apt')
print("Example 02: list(a_tuple): ", list(a_tuple))

# split() function
birthday = '1994/11/11'
print("Example 03: list(birthday): ", birthday.split('/'))


# append()  (加值)

# extend()  (加串列)

# insert()


# del，不能用 delete()

# remove()

# pop()
pop_list = ['data', 'engineering', 'test']

print('pop() : ', pop_list.pop())
print('pop(1) : ', pop_list.pop())


# index()

print('index() : ', pop_list.index('data'))


# in 

print('data' in pop_list)

# count()

print('count() : ', pop_list.count('data'))


# join 是 split 的相反
pop_list = ['data', 'engineering', 'test']
joined = '*'.join(pop_list)
split = joined.split('*')
print('join: ', joined)
print('split:', split)


# sort()

a_list = ['a', 'b', 'd', 'c']
a_list.sort()

print('sort list', a_list)


# copy

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]