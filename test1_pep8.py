# Input data
data = [
    {"name": "Alice", "age": "25", "city": "New York"},
    {"name": "Bob", "age": "thirty", "city": "Los Angeles"},
    {"name": "Charlie", "age": "35", "city": "Chicago"}
]

def age_to_int(data: list) -> list:
    """
    將年齡轉換為整數，並過濾掉無法轉換的數據。
    """
    for i in range(len(data) - 1, -1, -1):  # 從後往前迭代避免索引錯誤
        try:
            data[i]["age"] = int(data[i]["age"])  # 嘗試轉換年齡為整數
            del data[i]["city"]  # 移除 'city' 鍵
        except ValueError:  # 捕捉數值轉換錯誤
            del data[i]  # 無法轉換時刪除該元素
    return data


def age_to_int_v2(data: list) -> list:
    """
    使用列表推導式處理數據，將年齡轉換為整數，並過濾無法轉換的數據。
    """
    filtered_data = [
        {"name": item["name"], "age": int(item["age"])}
        for item in data
        if "age" in item and item["age"].isdigit()  # 確保 age 是可轉換的數字
    ]
    return filtered_data


if __name__ == "__main__":
    # 使用第一個方法處理數據
    result1 = age_to_int(data.copy())  # 使用副本避免原始數據被修改
    print("Result using age_to_int:", result1)

    # 使用第二個方法處理數據
    result2 = age_to_int_v2(data)
    print("Result using age_to_int_v2:", result2)
