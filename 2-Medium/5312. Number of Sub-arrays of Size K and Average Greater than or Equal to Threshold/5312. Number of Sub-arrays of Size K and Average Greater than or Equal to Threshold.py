class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        count = sum = 0
        right = k-1
        for i in range(0, k):
            sum += arr[i]
        while right < len(arr):
            if sum / k >= threshold:
                count += 1
            right += 1
            if right < len(arr)-1:
                sum += arr[right] - arr[right-k]
        return count


if __name__ == "__main__":
    solution = Solution()
    # arr = [2, 2, 2, 2, 5, 5, 5, 8]
    arr = [1, 1, 1, 1, 1]
    k = 1
    threshold = 0
    print(solution.numOfSubarrays(arr, k, threshold))
