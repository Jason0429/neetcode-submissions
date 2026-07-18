class Solution:
    def isValid(self, s: str) -> bool:
        # add all openings
        # pop when closing char is detected, but the top of the stack must not be empty or a mis-matching opening char

        closing_to_opening_char = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        def is_opening_char(c: str) -> bool:
            return c in closing_to_opening_char.values()

        def is_closing_char(c: str) -> bool:
            return c in closing_to_opening_char.keys()

        stack = list()

        for c in s:
            if is_opening_char(c):
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                top_stack = stack.pop()
                if top_stack != closing_to_opening_char[c]:
                    return False
        
        return len(stack) == 0
