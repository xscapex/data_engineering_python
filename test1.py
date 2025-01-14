# Input data
data = [
    {"name": "Alice", "age": "25", "city": "New York"},
    {"name": "Bob", "age": "thirty", "city": "Los Angeles"},
    {"name": "Charlie", "age": "35", "city": "Chicago"}
]

# 請撰寫一個函數，將年齡轉換為整數，並過濾掉無法轉換的數據。
# 輸出格式應為 [{"name": "Alice", "age": 25}, {"name": "Charlie", "age": 35}]

# 重點準備：

# try-except 處理數據清洗。
# 使用 Python 基本資料結構操作（如列表和字典）。
# 熟悉 JSON 格式處理。


print(data)

# range(start, stop, step)

def age_to_int(data: list) -> list:
    '''
    請撰寫一個函數，將年齡轉換為整數，並過濾掉無法轉換的數據。
    '''

    for i in range(len(data) - 1, -1, -1):
        try :
            # print(isinstance(int(data[1]['age']), int))
            data[i]['age'] = int(data[i]['age'])
            del data[i]['city']
            # print(data[i]['age'])
        except Exception as e:
            del data[i]
            # print({e})

    return data

def age_to_int_v2(data):
    filtered_data = [
        {"name": item["name"], "age": int(item["age"])}
        for item in data
        if item["age"].isdigit()
    ]

    return filtered_data


if __name__ == '__main__':

    filtered_data = [
    {"name": item["name"], "age": int(item["age"])}
    for item in data
    if item["age"].isdigit()
]
    print("filtered_data", filtered_data)
    result1 = age_to_int(data)
    print(result1)
    # result2 = age_to_int_v2(data)
    # print(result2)