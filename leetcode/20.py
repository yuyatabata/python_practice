class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        open_s = []

        for c in s:
            if c in open_brackets:
                open_s.append(c)
            else:
                if len(open_s) == 0:
                    return False
                o = open_s.pop()
                if open_brackets.index(c) != close_brackets.index(o):
                    return False
        return True
