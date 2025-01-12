# # 用 {} or dict() 來建立


# a_list = ['data', 'engineering', 'test']


# # data = {'name': 'Alice', 'age': 25}
# # data = {'name': 'Alice'}
# # assert 'name' in data and 'age' in data, "資料缺少必要的鍵"

# a_list = ['data', 'engineering', 'test']

# def list_dict(list: list):
#     try:
#         a_dict = dict(a_list)
#     except:
#         print('error')
#     finally:
#     # 清理操作
#         print("This will always run, cleaning up...")
#     return a_dict

# # def list_dict(list: list):

# #     a_dict = dict(a_list)
# #     return a_dict


# list_dict(a_list)

# if __name__ == '__main__':
#     print(list_dict(a_list))

    
# def list_dict(input_list: list):
#     a_dict = {}  # 預設為空字典，避免變數未定義的錯誤
#     try:
#         a_dict = dict(input_list)  # 嘗試將 list 轉換為字典
#     except ValueError:  # 捕捉具體的錯誤類型
#         print('錯誤：不能將此列表轉換為字典')
#     finally:
#         # 如果有需要進行清理的操作，可以放在這裡
#         print("清理操作：這段程式碼總是會執行")
#     return a_dict  # 回傳處理結果，無論是否成功

# # 測試
# a_list = ['data', 'engineering', 'test']
# result = list_dict(a_list)
# print(result)

# if __name__ == '__main__':
#     # 確保在主程式中運行
#     print(list_dict(a_list))






import traceback

def list_dict(input_list: list):
    a_dict = {}  # 預設為空字典，避免變數未定義的錯誤
    try:
        a_dict = dict(input_list)  # 嘗試將 list 轉換為字典
    except Exception as e:  # 捕捉所有異常
        print(f'發生錯誤: {str(e)}')  # 打印錯誤訊息
        traceback.print_exc()  # 打印完整的錯誤堆棧跟蹤
    finally:
        # 如果有需要進行清理的操作，可以放在這裡
        print("清理操作：這段程式碼總是會執行")
    return a_dict  # 回傳處理結果，無論是否成功


if __name__ == '__main__':
    # 確保在主程式中運行
    a_list = ['data', 'engineering', 'test']
    print(list_dict(a_list))
