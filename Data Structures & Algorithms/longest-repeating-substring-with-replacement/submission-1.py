class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        letter_to_count = dict()

        l = 0
        most_freq_letter_count = 0
        for r in range(len(s)):
            letter_to_count[s[r]] = letter_to_count.get(s[r], 0) + 1
            most_freq_letter_count = max(most_freq_letter_count, letter_to_count[s[r]])

            if (r - l + 1) - most_freq_letter_count > k:
                letter_to_count[s[l]] -= 1
                l += 1
        
        return (r - l + 1)





