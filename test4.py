# 給定一個大列表，找出所有和為目標值的數字對。
nums = [2, 7, 11, 15, -2, 8, 10]
target = 9

# 請撰寫函數，返回所有符合條件的數字對。
# 輸出格式應為 [(2, 7), (-2, 11)]

# 重點準備：

# 使用集合或字典提高效率。
# 善用 Python 的迭代器與生成器。

def find_pairs(nums, target):
    seen = set()  # 用來記錄已經遇過的數字
    for num in nums:
        complement = target - num
        if complement in seen:  # 如果補數存在，則找到一對數字
            yield (complement, num)  # 使用生成器返回配對
        seen.add(num)  # 把當前數字加入已遇見的數字集合

# 測試
pairs = list(find_pairs(nums, target))  # 將生成器轉換為列表
print(pairs)  # 輸出：[(2, 7), (-2, 11)]



# 解釋：
# 使用 seen 集合來記錄已遍歷過的數字。
# 在遍歷每一個數字時，計算它的補數（即 target - num）。
# 如果補數已經在 seen 集合中，則找到了符合條件的一對數字，並通過 yield 返回這一對。
# 否則，將當前數字加入 seen 集合。
# 使用生成器 yield 來延遲返回配對，這樣可以避免一次性將所有配對存儲在內存中，對於大資料集來說非常有用。
# 這樣的解法能夠以線性時間 O(n) 完成，並且具有很高的效率。