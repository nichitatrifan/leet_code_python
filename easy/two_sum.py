#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            for j, next_val in enumerate(nums[i+1:]):
                if val + next_val == target:
                    answer = [i, j+i+1]
                    return answer
        return []


if __name__ == '__main__' :
    solution = Solution()
    print(solution.twoSum([3,3],6))