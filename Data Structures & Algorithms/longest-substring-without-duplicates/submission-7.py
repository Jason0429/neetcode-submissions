class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        substring_window = set()

        l = 0
        for r in range(len(s)):
            while s[r] in substring_window:
                substring_window.remove(s[l])
                l += 1

            substring_window.add(s[r])
            longest_length = max(longest_length, r - l + 1)

        return longest_length