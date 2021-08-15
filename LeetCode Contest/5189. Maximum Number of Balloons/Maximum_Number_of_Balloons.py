class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
#         balon
        balloon_dict = dict()
        balloon_list = list("balon")
        for i in balloon_list:
            balloon_dict[i] = 0
        for i in list(text):
            if i == 'b' or i == 'a' or i == 'l' or i == 'o' or i == 'n':
                balloon_dict[i] += 1
        
        # print(balloon_dict.keys())
        # print(min(balloon_dict.keys(), key=(lambda k: balloon_dict[k])))
        for k, v in balloon_dict.items():
            print(k,v)

        min_key = min(balloon_dict, key = balloon_dict.get)
        print(min_key)
        min_value = balloon_dict[min_key]
        print("min_value", min_value)
        min_value = balloon_dict[min(balloon_dict, key = balloon_dict.get)]
        if min_value == 0:
            return 0
        else:
            min_l_o = min(balloon_dict['l'], balloon_dict['o'])
            # print(min_l_o)
            return min_l_o//2
        # if min_key == 'l' or min_key == 'o':
        #     return balloon_dict[min_key]
        # if balloon_dict['l'] >= min_value * 2 and balloon_dict['o'] >= min_value * 2:
        #     return min_value
        # else:
        #     return min_value - 1
 
    
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
solution = Solution()
print(solution.maxNumberOfBalloons(text))

