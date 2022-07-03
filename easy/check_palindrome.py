# Check if a number is palindrome
# Given an integer x, return true if x is palindrome integer.


class Solution:
    def isPalindrome(self, num: int) -> bool:
        x = num
        if num < 0:
            return False
        if num < 10:
            return True

        rev_num = 0
        while num > 0:
            mod_div = num % 10
            num = num // 10
            rev_num = (rev_num * 10) + mod_div

        if rev_num == x:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))