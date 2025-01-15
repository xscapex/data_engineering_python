test1 = 'Data engineering test'


# replace()
print('test 1 replace', test1.replace('test', 'test1'))

# len ()


# split()


# range()


# startwith()

print('test1 start with Data?', test1.startswith('Data'))
print('test1 start with Data?', test1.startswith('data'))

# zip()

## Scenario 1
cols = ['name', 'age', 'city']
values = ['Monica', '18', 'Taipei']

result = dict(zip(cols, values))

print(result)


## Scenario 2

file1_data = ['row1_file1', 'row2_file1', 'row3_file1']
file2_data = ['row1_file2', 'row2_file2', 'row3_file2']

# 合併兩個文件的對應行
for line1, line2 in zip(file1_data, file2_data):
    print(f"{line1} | {line2}")


## Scenario 3 
    
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, None]  # 有缺失數據

# 過濾掉 None 的數據
cleaned_data = [(name, score) for name, score in zip(names, scores) if score is not None]
print(cleaned_data)




# globals()
# locals()

def show_globals():
    print(globals())  # 查看全域命名空間
    print("Value of x:", globals()["scores"])  # 直接存取全域變數

show_globals()