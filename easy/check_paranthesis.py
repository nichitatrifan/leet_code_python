from concurrent.futures.process import _chain_from_iterable_of_lists
from inspect import stack


class Solution:
    def isValid(self, s: str) -> bool:
        left_stack = []
        s = s.replace(' ', '')
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in ['{', '[', '(']:
                left_stack.append(char)
            elif char == '}' and len(left_stack) != 0:
                bracket = left_stack.pop()
                if bracket != '{':
                    return False
            elif char == ']' and len(left_stack) != 0:
                bracket = left_stack.pop()
                if bracket != '[':
                    return False
            elif char == ')' and len(left_stack) != 0:
                bracket = left_stack.pop()
                if bracket != '(':
                    return False
            elif char in [']', '}', ')'] and len(left_stack) == 0:
                return False

        if len(left_stack) != 0:
            return False

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('}'))