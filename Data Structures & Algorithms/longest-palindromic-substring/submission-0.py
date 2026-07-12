class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        For an odd result, use each letter as the midpoint of a potential palindrome
        For an even result, use each letter and its neighbor as the midpoints of the potential palindrome
        Span outwards as long as substring is a valid palindrome
        Update res as you go
        '''

        res = ""
        resLen = 0

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res