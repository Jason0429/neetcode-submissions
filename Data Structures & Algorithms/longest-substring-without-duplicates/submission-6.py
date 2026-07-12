class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Keep track of longest substring length
        Keep set of letters in window
        while s[r] in window, remove s[l] and l++
        Update longest
        '''

        res = 0
        window = set()
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            res = max(res, r - l + 1)

        return res