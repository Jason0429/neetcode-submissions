class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Push opening characters to a stack
        If closing character, pop the corresponding opening character from stack
            if not corresponding opening character, return False
            if stack is empty, return False
        return stack is empty as boolean
        '''

        stack = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                continue
            
            if not stack:
                return False
            
            last = stack.pop()
            if last != close_to_open[c]:
                return False

        return not stack
            
