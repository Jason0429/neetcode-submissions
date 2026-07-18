class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        See if the left and right pointed to characters match.
        If so, continue inwards by moving them both.
        If they ever mismatch, return False.
        The iteration stopping criteria is when left idx > right idx.
        A simpler way to represent this loop is to traverse up to the middle with the left pointer (l)
        and get the right pointer with (len - l - 1)
        '''
        s = ''.join(char.lower() for char in s if char.isalnum())
        length = len(s)

        for leftIdx in range(length // 2):
            if s[leftIdx] != s[length - leftIdx - 1]:
                return False
        
        return True
