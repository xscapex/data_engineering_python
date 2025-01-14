# 考題類型： 模擬多任務處理，使用 Python 的並行工具處理數據。

import time

def process_task(task_id):
    time.sleep(1)
    return f"Task {task_id} completed"

# 實作一個函數，同時處理 5 個任務。
# 輸出格式應為 ["Task 1 completed", "Task 2 completed", ...]

# 重點準備：

# 熟悉 concurrent.futures 或 multiprocessing。
# 使用 ThreadPoolExecutor 進行並行處理。

f