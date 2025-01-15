from datetime import datetime

def calculate_minute_averages(stream):
    # 使用普通字典來聚合每分鐘的值
    minute_data = {}

    # 將每個數據按分鐘聚合
    for entry in stream:
        # 解析 timestamp，並只取分鐘部分
        timestamp = datetime.fromisoformat(entry["timestamp"][:-1])  # 去掉 Z
        print(timestamp)
        minute_key = timestamp.strftime("%Y-%m-%dT%H:%M")

        # 手動檢查鍵是否存在，若不存在則初始化為空列表
        if minute_key not in minute_data:
            minute_data[minute_key] = []

        # 將值加入對應的分鐘
        minute_data[minute_key].append(entry["value"])

    # 計算每分鐘的平均值
    result = []
    for minute, values in minute_data.items():
        average = sum(values) / len(values)
        result.append({"minute": minute, "average": average})

    return result

# 測試資料
stream = [
    {"timestamp": "2025-01-01T10:00:00Z", "value": 10},
    {"timestamp": "2025-01-01T10:00:00Z", "value": 20},
    {"timestamp": "2025-01-01T10:01:00Z", "value": 20},
    {"timestamp": "2025-01-01T10:02:00Z", "value": 15}
]

# 呼叫函數並打印結果
output = calculate_minute_averages(stream)
print(output)
