class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result = 0
        for i in range(1,len(s)+1):
            for j in range(len(s)-i+1):
                if i == len(set(s[j:j+i])):
                    result = max(result,i)
                    break
            else:
                return result
        return result

## best solution
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength