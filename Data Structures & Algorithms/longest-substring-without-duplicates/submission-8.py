class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return the length of the longest substring without duplicating characters
        # since there can't be duplicates, we can use a dict for [char: index]
        # add to the window if the next character is not a duplicate
        # if the next character is a duplicate, remove all characters in the window up to and including the first duplicate char

        longest_length = 0
        l = 0
        window_set = set()

        for r in range(len(s)):
            while s[r] in window_set:
                window_set.remove(s[l])
                l += 1
            window_set.add(s[r])
            longest_length = max(longest_length, r - l + 1)
        
        return longest_length
