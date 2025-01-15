import logging

logging.basicConfig(level=logging.INFO)

def log_execution(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Result: {result}")
        return result
    return wrapper

@log_execution
def transform_data(data):
    return [x * 2 for x in data]

transform_data([1, 2, 3])
