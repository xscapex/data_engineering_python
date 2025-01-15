# 考題類型： 基本算法題目，比如排序、二分搜索、圖算法。
# 給定一個升序排列的列表和一個目標值，找到目標值的索引。
nums = [1, 3, 5, 7, 9]
target = 10

# 若找到目標值，返回其索引；否則返回 -1。
# 重點準備：

# 熟悉基礎排序和搜索算法。
# 能高效操作列表和數據結構。

def find_target(nums, target) -> int:

    for num in nums:
        if num == target:
            return nums.index(num)
    else:
        return -1
    
    

if __name__ == '__main__':

    result = find_target(nums, target)
    print(result)