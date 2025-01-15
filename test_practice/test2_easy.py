import re

# 假設一組雲端記錄的批次數據：
logs = [
    "2025-01-01 10:00:00 - user1 - login",
    "2025-01-01 10:05:00 - user2 - login",
    "2025-01-01 10:10:00 - user1 - login"
]



def count_logins(logs: list) -> dict :

    # 請撰寫一個函數，統計每個用戶的登錄次數。
    # 輸出格式應為 {"user1": 1, "user2": 0}

    login_count = {}

    for log in logs:

        user = log.split(' - ')[1]
        action = log.split(' - ')[2]
        
        if user not in login_count:
            # 初始化每個用戶的登錄次數為 0
            login_count[user] = 0

        if action == "login":
            # 若操作為登錄則累加次數
            login_count[user] += 1
    
    return login_count


if __name__ == "__main__":

    # 調用函數
    result = count_logins(logs)
    print(result)