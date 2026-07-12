class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_anagrams = dict()

        for s in strs:
            s_hash = self.get_hash(s)
            if s_hash in hash_to_anagrams:
                hash_to_anagrams[s_hash].append(s)
            else:
                hash_to_anagrams[s_hash] = [s]
            
        return hash_to_anagrams.values()

    def get_hash(self, s: str) -> str:
        encoding = [0] * 26
        
        for c in s:
            encoding[ord(c) - ord('a')] += 1
        
        return str(encoding)
