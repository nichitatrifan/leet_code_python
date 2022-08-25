# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
# 'digits' does not contain any leading 0's.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry:
            digits[i] += 1
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            if carry and i - 1 < 0:
                digits = [carry] + digits
                break
            i -= 1
        return digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9]))