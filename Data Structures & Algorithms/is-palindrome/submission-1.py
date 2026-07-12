class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c.lower() for c in s if c.isalnum())

        for i in range(len(clean_s) // 2):
            if clean_s[i] != clean_s[-i-1]:
                return False
        
        return True