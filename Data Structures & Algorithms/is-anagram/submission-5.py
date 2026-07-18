class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: contains same characters & frequency of characters of each other in any order

        if len(s) != len(t):
            return False

        # hashmap to count freq of word A
        # hashmap to count freq of word B
        # check if hashmaps match: True

        freq_a = dict()
        freq_b = dict()

        for i in range(len(s)):
            freq_a[s[i]] = freq_a.get(s[i], 0) + 1
            freq_b[t[i]] = freq_b.get(t[i], 0) + 1

        return freq_a == freq_b