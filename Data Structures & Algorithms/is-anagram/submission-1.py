class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A = ord('a')
        s_count = [0] * 26
        t_count = [0] * 26

        for c in s:
            s_count[ord(c) - A] += 1
        
        for c in t:
            t_count[ord(c) - A] += 1
        
        return str(s_count) == str(t_count)