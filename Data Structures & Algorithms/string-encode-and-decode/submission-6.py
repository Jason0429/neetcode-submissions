class Solution:


    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while l < len(s):
            # compute count
            r = l + 1
            while s[r] != "#":
                r += 1
            
            count = int(s[l:r])
            word = s[r + 1: r + 1 + count]
            res.append(word)

            l = r + 1 + count
        
        return res
        