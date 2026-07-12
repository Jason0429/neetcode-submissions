class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = dict()
        t_count = dict()

        for letter in s:
            s_count[letter] = s_count.get(letter, 0) + 1
        
        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1

        for letter, freq in s_count.items():
            if letter not in t_count or freq != t_count[letter]:
                return False

        return True