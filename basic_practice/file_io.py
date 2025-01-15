
# 1. writelines() 的作用
# 功能: 一次性將一個可迭代對象（如列表或生成器）中的多行內容寫入文件。
# 對應於: readlines()，因為它們都處理「多行」的數據。


lines_to_write = ["Hello, World!\n", "This is line 2.\n", "This is line 3.\n"]

# 測試 write() 的結果 => 就會發現會報錯，
with open("output01.txt", "w") as f:
    try:
        f.write(lines_to_write)
    except TypeError as e:
        print('error occured!!', {e})
    finally:
        # with open() 不需要手動關閉檔案，Python 會自動處理。
        # f.close()
        print("with open() 不需要手動關閉檔案，Python 會自動處理。")

# 測試 writelines() 的結果
with open("output02.txt", "w") as f:
    f.writelines(lines_to_write)


print(local())