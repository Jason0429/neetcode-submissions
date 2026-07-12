class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        longest_length_without_duplicates = 1
        window_letter_set = { s[0] }
        
        l = 0
        for r in range(1, len(s)):
            # move left up until no more repeats in window
            while s[r] in window_letter_set:
                window_letter_set.remove(s[l])
                l += 1
            
            window_letter_set.add(s[r])
            longest_length_without_duplicates = max(longest_length_without_duplicates, r - l + 1)

        return longest_length_without_duplicates