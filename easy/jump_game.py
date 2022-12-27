# You are given an integer array 'nums'.
# You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        current = len(nums) - 1
        previous = len(nums) - 2

        while previous >= 0:
            if previous + nums[previous] >= current:
                current = previous
                previous -= 1
            else:
                previous -= 1
        if current == 0:
            return True
        else:
            return False

    def canJump2(self, nums: List[int]) -> bool:
        # works, but exceeds the time limit
        # there is a recursive slution that works, but not this one
        def check(nums: List[int], i: int) -> bool:
            if i >= len(nums) - 1:
                return True
            elif nums[i] == 0 and i < len(nums) - 1:
                return False
            else:
                result = False
                for k in range (nums[i], 0, -1):
                    result = result or check(nums, i + k)
                return result
        return check(nums, 0)

if __name__ == '__main__':
    # [2,5,0,0]
    # [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    solution = Solution()
    print(solution.canJump([2,5,0,0]))