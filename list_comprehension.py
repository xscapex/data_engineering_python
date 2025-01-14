# Generate a 0-6 list
list1 = list(range(0,7))
print(list1)

# Original method

list2 = []

for i in range(0,7):
    list2.append(i)


# [運算式 for 項目 in 可迭代項目]

list3 = [ num for num in range(0, 7)]
print(list3)

list4 = [ num-1 for num in range(0, 7)]
print(list4)


list5 = [ num-1 for num in range(0, 7) if num % 2 == 0]
print(list5)

list6 = [(row, col) for row in range(0,3) for col in range(0, 3)]
print(list6)

