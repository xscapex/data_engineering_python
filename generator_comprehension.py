

# def numbers():
#     yield from range(5)

# def squares():
#     for num in numbers():
#         yield num ** 2

# print(list(squares()))  # Output: [0, 1, 4, 9, 16]



def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
    
ranger = my_range(1, 5)
print(ranger)