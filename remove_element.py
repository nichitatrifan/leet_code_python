# Runtime: 58 ms, faster than 11.74% of Python3 online submissions for Remove Element.
# Memory Usage: 13.6 MB, less than 99.99% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums, val: int) -> int:
        count = 0
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums[length - 1], nums[i] = nums[i], nums[length - 1]
                length -= 1
            else:
                i += 1
        print(nums)
        return length
        
        


if __name__ == '__main__':
    solution = Solution()
    new_list = [1,1,1,1,2,2,2,2,2,3,2]
    print(solution.removeElement(new_list, 1))
