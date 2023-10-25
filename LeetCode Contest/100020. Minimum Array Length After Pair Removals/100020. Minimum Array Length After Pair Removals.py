def minimumLengthAfterOperations(nums):
    n = len(nums)
    can_remove = True  # 用來標記是否還可以執行操作
    while can_remove:
        can_remove = False  # 先假設無法再執行操作
        new_nums = []
        i = 0
        while i < n:
            if i < n - 1 and nums[i] < nums[i + 1]:
                # 如果找到一對符合條件的元素，則可以執行操作
                can_remove = True
                i += 2  # 跳過下一個元素
            else:
                new_nums.append(nums[i])  # 保留元素
                i += 1
        nums = new_nums
        n = len(nums)  # 更新陣列長度
    return n  # 返回最終的陣列長度

# 測試
nums = [2,3,4,4,4]
result = minimumLengthAfterOperations(nums)
print(result)  # 此處輸出應為 1
