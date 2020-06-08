class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anas = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s in anas:
                anas[s].append(string)
            else:
                anas[s] = [string]
        return [anas[x] for x in anas]


if __name__ == "__main__":
    solution = Solution()
    my_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams((my_list)))
