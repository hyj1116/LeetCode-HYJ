class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        count = 0
        for word in words:
            if word != "" and word != '-':
                isToken = True
                for ch in word:
                    if ch.isdigit():
                        isToken = False
                        break
                if isToken:
                    if word.count('-') == 1:
                        hyphen_loc = word.index('-')
                        if hyphen_loc != 0 and hyphen_loc != len(word):
                            if word[hyphen_loc-1].isalpha() and word[hyphen_loc+1].isalpha():
                                if word.count('!') == 1:
                                    if word.index('!') == len(word)-1:
                                        count += 1
                                if word.count('!') == 0:
                                    count += 1
                    if word.count('-') == 0:
                        if word.count('!') == 1:
                            if word.index('!') == len(word)-1:
                                count += 1
                        if word.count('!') == 0:
                            count += 1
        return count


sol = Solution()
s = ",aab"
res = sol.countValidWords(s)
print(res)
