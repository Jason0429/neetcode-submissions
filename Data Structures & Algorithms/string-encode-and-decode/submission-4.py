class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])


    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        '''
        Use two pointers
        Move right pointer until it hits #
        length = int([l:r])
        word is located at s[r+1: r+length]
        move l = r+1
        move r = l+1
        append the word
        ^ do while i < len(s)
        '''

        while l < len(s):
            r = l + 1
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            word = s[r+1:r+length+1]
            res.append(word)
            l = r + length + 1

        return res
