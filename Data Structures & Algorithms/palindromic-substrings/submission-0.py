class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Perform the following twice (odd and even palindrome cases):

        Use each letter as the midpoint of a potential palindrome
        Increment result as long as the window is a palindrome
        '''
        res = 0

        # odd
        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        # even
        for i in range(len(s)):
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res