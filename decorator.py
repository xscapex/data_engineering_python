def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 在這裡添加額外的行為
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")
        return result
    return wrapper


# def my_decorator(func,*args, **kwargs):
#     print("Before the function is called")
#     result = func(*args, **kwargs)
#     print("After the function is called")
#     return result



@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")




