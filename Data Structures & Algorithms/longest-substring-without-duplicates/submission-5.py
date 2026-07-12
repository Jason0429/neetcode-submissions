class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Keep sliding window of substring without duplicates
        Use a set to keep track of all the letters in the window
        When visiting a new letter, remove the left side of the string until that 
        letter is no longer in the window, then add the new letter and to the set
        Maximize longest substring along the way
        '''

        res = 0
        l = 0
        window = set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
                
            window.add(s[r])
            res = max(res, r - l + 1)

        return res