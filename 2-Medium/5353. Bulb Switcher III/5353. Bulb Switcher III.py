class Solution:
    def numTimesAllBlue(self, light):
        status = [0] * len(light)
        count = 0
        for i in light:
            status[i-1] = 1
            last_tail = 0
            shine = 0
            for j in range(last_tail, len(light)):
                if status[j] != 0:
                    shine += 1
                else:
                    break
            for k in range(last_tail, last_tail+shine):
                status[k] = 2
            if 1 not in status:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    light = [2, 1, 4, 3, 6, 5]
    print(solution.numTimesAllBlue(light))
