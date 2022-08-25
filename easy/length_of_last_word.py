# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '
# There will be at least one word in s

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sent_len = len(s) - 1
        space_len = 0
        start = False

        while sent_len != 0:
            if not start and s[sent_len] == ' ':
                space_len += 1
            elif not start and s[sent_len] != ' ':
                start = True
            if s[sent_len] == ' ' and start:
                return len(s) - sent_len - space_len - 1
            sent_len -= 1
        return len(s) - sent_len - space_len

    def lengthOfLastWord_solution2(self, s: str) -> int:
        sent_len = len(s) - 1
        word_len = 0
        start = False

        while sent_len >= 0:
            if s[sent_len] == ' ' and not start:
                sent_len -= 1
            elif s[sent_len] != ' ' and not start:
                start = True
            elif s[sent_len] == ' ' and start:
                return word_len
            elif s[sent_len] != ' ' and start:
                word_len += 1
                sent_len -= 1
        return word_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord('World '))
    print(solution.lengthOfLastWord_solution2('World '))