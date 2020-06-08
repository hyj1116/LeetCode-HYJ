class Solution:
    def backspaceCompare(self, S, T):
        stack_S = []
        stack_T = []
        for i in S:
            if i == "#" and len(stack_S) > 0:
                stack_S.pop()
            else:
                stack_S.append(i)
        for i in T:
            if i == "#" and len(stack_T) > 0:
                stack_T.pop()
            else:
                stack_T.append(i)
        if len(stack_S) == len(stack_T):
            for i in range(len(stack_S)):
                if stack_S[i] != stack_T[i]:
                    return False
            return True
        else:
            return False

solution=Solution()
