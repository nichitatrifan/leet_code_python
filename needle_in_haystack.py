class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)

        for i in range(0,haystack_len - needle_len + 1):
            if haystack[i: i + needle_len] == needle:
                return i
        
        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr('mississippi', 'issip'))
