class Solution:
    def minJumps(self, arr: List[int]) -> int:
        index = 0
        while(index != len(arr)-1):
            if arr.count(arr, arr[index]) > 1:
                index = 
