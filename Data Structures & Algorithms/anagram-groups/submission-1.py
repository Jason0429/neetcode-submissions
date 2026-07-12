class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        def anagram_hash(s):
            A = ord('a')
            count = [0] * 26

            for c in s:
                count[ord(c) - A] += 1
            
            return str(count)


        for s in strs:
            ahash = anagram_hash(s)
            anagrams[ahash] = anagrams.get(ahash, [])
            anagrams[ahash].append(s)

        return anagrams.values()