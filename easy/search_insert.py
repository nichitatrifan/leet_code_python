# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1

        found = False
        low_index = 0
        high_index = len(nums) - 1

        while not found:
            mid_index = (low_index + high_index) // 2
            if nums[mid_index] == target:
                found = True
            elif high_index - low_index == 1:
                if target > nums[high_index]:
                    mid_index = high_index + 1
                elif target < nums[low_index]:
                    mid_index = low_index - 1 if low_index != 0 else 0
                else:
                    mid_index = low_index + 1
                found = True
            elif nums[mid_index] > target:
                high_index = mid_index
            elif nums[mid_index] < target:
                low_index = mid_index
        return mid_index

if __name__ == '__main__':
    solution = Solution()
    # result = solution.searchInsert([2,3,4,5,6,7,8,9,10,11,12,13,14,15], 1)
    result = solution.searchInsert([1], 1)
    print(result)
