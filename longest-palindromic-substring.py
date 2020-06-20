class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)+1,0,-1):
            for j in range(len(s)-i+1):
                if s[j:j+i] == s[j:j+i][::-1]:
                    answer = s[j:j+i]
                    break
            if answer:
                break
        return answer