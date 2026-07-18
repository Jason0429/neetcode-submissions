class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: contains same characters & frequency of characters of each other in any order

        # hashmap to count freq of word A
        # hashmap to count freq of word B
        # check if hashmaps match: True

        freq_a = dict()
        freq_b = dict()

        for letter in s:
            freq_a[letter] = freq_a.get(letter, 0) + 1
        
        for letter in t:
            freq_b[letter] = freq_b.get(letter, 0) + 1

        # number of unique characters should be the same
        if len(freq_a) != len(freq_b):
            return False

        for letter, count in freq_a.items():
            if letter not in freq_b:
                return False
            
            if freq_b[letter] != count:
                return False
        
        return True