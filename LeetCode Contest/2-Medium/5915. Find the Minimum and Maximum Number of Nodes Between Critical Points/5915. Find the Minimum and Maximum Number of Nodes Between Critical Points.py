# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if head == None:
            return [-1, -1]
        arr = []
        idx = 1
        while head.next and head.next.next:
            idx += 1
            prev = head
            head = head.next
            # print(prev.val)
            if (prev.val < head.val and head.val < head.next.val) or (prev.val > head.val and head.val > head.next.val):
                print(head.val)
                arr.append(idx)

        if len(arr) < 2:
            return [-1, -1]
        else:
            minnum = 0
            for i in range(1, len(arr)):
                minnum = min(arr[i]-arr[i-1], minnum)
        return [minnum, (arr[len(arr)-1] - arr[0])]


sol = Solution()
nums = [5, 3, 1, 2, 5, 1, 2]
res = sol.nodesBetweenCriticalPoints(nums)
print(res)
