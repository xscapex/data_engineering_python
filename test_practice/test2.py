import re

# 假設一組雲端記錄的批次數據：
logs = [
    "2025-01-01 10:00:00 - user1 - login",
    "2025-01-01 10:05:00 - user2 - login",
    "2025-01-01 10:10:00 - user1 - login"
]

# 請撰寫一個函數，統計每個用戶的登錄次數。
# 輸出格式應為 {"user1": 1, "user2": 0}


login_count = {}  # 使用普通字典

# 正規表達式模式
pattern = r" - (user\d+) - login"

# 遍歷日誌
for log in logs:
    match = re.search(pattern, log)
    print(match)
    print(match.group(1))
    if match:
        user = match.group(1)
        if user in login_count:
            login_count[user] += 1  # 累加登錄次數
        else:
            login_count[user] = 1  # 初始化計數




# 函數來統計每個用戶的登錄次數
def count_logins(logs):
    login_count = {}  # 使用普通字典
    
    # 正規表達式模式
    pattern = r" - (user\d+) - login"
    
    # 遍歷日誌
    for log in logs:
        match = re.search(pattern, log)
        if match:
            user = match.group(1)
            if user in login_count:
                login_count[user] += 1  # 累加登錄次數
            else:
                login_count[user] = 1  # 初始化計數
    
    return login_count

# # 呼叫函數並打印結果
# result = count_logins(logs)
# print(result)
