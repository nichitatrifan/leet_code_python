# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# 1-solution: Sort the array of strings in alphabetical order. Compare first and last element in the array
# 2-solution: Take first element as a prefix. Compare with the rest of the arrays abd delete parts of the word that do not match

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        if prefix == '':
            return ''
        for word in strs[1:]:
            if word == '':
                return ''
            if word[0] == prefix[0]:
                i = 1
                j = 1
                while prefix[:i] == word[:j] and i<len(prefix) and j<len(word):
                    i += 1
                    j += 1
                if prefix[i-1] != word[j-1]:
                    prefix = prefix[:i-1]
                else:
                    prefix = prefix[:i]
            else:
                return ''
        return prefix


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["dog","racecar","car"]))