from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr, difference):
        """Brute force
        """
        arr = list(set(arr))
        # if difference < 0:
        # arr.reverse
        # res_dict = defaultdict(int)
        res, maximum = 1, 0
        # for i in range(len(arr)):
        for i in range(len(arr)):
            res = 1
            j = i
            while j < len(arr):
                if arr[j] + difference in arr:
                    res += 1
                    j += difference
            if maximum > res:
                res = maximum
        # for i in range(len(res_dict)):
        #     if res_dict[i] > maximum:
        #         maximum = res_dict[i]
        return maximum
        # return res if res > 1 else 1


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """Brute force
        """
        # arr=list(set(arr))
        s = set(arr)
        # if difference < 0:
        # arr.reverse
        # res_dict = defaultdict(int)
        count, maximum = 1, 1
        res_dict = {}
        for i in arr:
            count = 0
            k = i
            while k in s:
                s.remove(k)
                k += difference
                count += 1
            if count > maximum:
                maximum = count
        return maximum
