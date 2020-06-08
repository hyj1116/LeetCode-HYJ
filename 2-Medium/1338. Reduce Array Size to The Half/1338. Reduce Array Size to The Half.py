class Solution:
    def minSetSize(self, arr):
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        values = []
        for i in dic.values():
            values.append(i)
        values.sort(reverse=True)
        count = res = 0
        for i in values:
            res += i
            count += 1
            if res >= len(arr) // 2:
                return count


if __name__ == "__main__":
    solution = Solution()
    my_list = [1, 9]
    print(solution.minSetSize(my_list))


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0

        for index, count in enumerate(sorted(collections.Counter(arr).values(), reverse=True)):
            total_count += count

            if total_count >= len(arr) // 2:
                return index + 1

        return 0
