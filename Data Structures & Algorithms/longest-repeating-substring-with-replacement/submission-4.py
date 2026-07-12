class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Store window mapping letter to count
        Keep track of the most frequent letter count
        add right letter
        update right letter count
        update most_freq_letter_count = max(most_freq_letter_count, right letter)

        # "if" not "while" because the max length should not change unless we
        add a right letter that actually exceeds the most_freq_letter_count
        
        if window length - most_freq_letter_count > k:
            drop left letter
            update left letter count
        '''

        res = 1
        letters_to_count = { s[0] : 1 }
        most_freq_count = 1

        l = 0
        for r in range(1, len(s)):
            letters_to_count[s[r]] = letters_to_count.get(s[r], 0) + 1
            most_freq_count = max(most_freq_count, letters_to_count[s[r]])
            if (r - l + 1) - most_freq_count > k:
                letters_to_count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res