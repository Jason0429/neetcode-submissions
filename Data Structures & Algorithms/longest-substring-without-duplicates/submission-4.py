class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Keep sliding window of substring without duplicates
        Use a set to keep track of all the letters in the window
        When visiting a new letter, remove the left side of the string until that 
        letter is no longer in the window, then add the new letter and to the set
        Maximize longest substring along the way
        '''

        if len(s) == 0:
            return 0

        res = 1
        l = 0
        window = { s[0] : 1 }

        for r in range(1, len(s)):
            while s[r] in window:
                window[s[l]] -= 1
                
                if window[s[l]] == 0:
                    del window[s[l]]
                
                l += 1
                
            window[s[r]] = window.get(s[r], 0) + 1
            res = max(res, r - l + 1)

        return res