class Solutio:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = 1
        ans = 
        ans[0] = L
        for i in range(1, len(nums)):
            ans[i+1] = ans[i]*nums[i]
        R = 1
        for i in reversed(range(len(nums))):
            ans[i] *= R
            R *= nums[i]
        return ans

import random
from typing import List
if __name__ == "__main__":
    solution = Solution()
    my_list = random.choices(range(20), k=10)
    print(solution(my_list))
    
