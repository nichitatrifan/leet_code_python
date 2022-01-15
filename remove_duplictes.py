from typing import List


class Solution:
     def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
               j += 1
            else:
			  #  i moves only when a distinct value is found in the list. 
               i += 1
               nums[i] = nums[j]
               j += 1 
        return i+1
        

if __name__ == '__main__':
    solution = Solution()
    new_list = [1,1,2,2,3,3,4,5,6]
    print(solution.removeDuplicates(new_list))