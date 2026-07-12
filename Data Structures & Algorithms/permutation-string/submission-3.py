class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        FULL_MATCH = 26
        

        # create count of s1 and s2[:len(s1)]
        s1_count = [0] * FULL_MATCH
        window_count = [0] * FULL_MATCH

        def get_idx(letter):
            return ord(letter) - ord("a")

        for i in range(len(s1)):
            s1_count[get_idx(s1[i])] += 1
            window_count[get_idx(s2[i])] += 1

        # check how many matches there currently are
        matches = 0
        for i in range(FULL_MATCH):
            matches += 1 if s1_count[i] == window_count[i] else 0

        # move window over until full match
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == FULL_MATCH:
                return True

            l_idx = get_idx(s2[l])
            r_idx = get_idx(s2[r])

            # remove left letter
            window_count[l_idx] -= 1
            if s1_count[l_idx] == window_count[l_idx]:
                matches += 1
            # only decrement matches if it was already a match and removing the left letter got it unmatched
            elif s1_count[l_idx] == window_count[l_idx] + 1:
                matches -= 1

            # add right letter
            window_count[r_idx] += 1
            if s1_count[r_idx] == window_count[r_idx]:
                matches += 1
            # only decrement matches if it was already a match and adding the right letter got it unmatched
            elif s1_count[r_idx] == window_count[r_idx] - 1:
                matches -= 1

            # keep sliding window over
            l += 1

        # no permutation match
        return matches == FULL_MATCH
