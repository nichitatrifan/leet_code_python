# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# nums1 size is len(nums1) + len(nums2)

from typing import List

class Solution:
    def merge_better(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merging two sorted arrays into the first one

        The idea is to start merging from the back of the nums1 array
        in order to avoid squared complexity. Whenever we run out of the
        elements from the second array siply stop

        Args:
            nums1 (List[int]): array where the values are stored
            m (int): current used space
            nums2 (List[int]): array to merge
            n (int): number of elements
        """
        i = m - 1
        j = n - 1
        for k in range(m + n - 1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        insert = 0

        while i < m + n and j < n:
            if i >= m + insert and nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                for k in range(m+n-1, i, -1):
                    nums1[k] = nums1[k - 1]
                nums1[i] = nums2[j]
                j += 1
                i += 1
                insert += 1

    def merge_pythonic_list_concept(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1 = nums2
            return

        i = 0 # i, m for the first list
        j = 0 # j, n for the second list

        while i <= m and j < n:
            if i == m and j < n:
                nums1.append(nums2[j])
                j += 1
                m += 1
            elif nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
                m += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                i += 1


if __name__ == '__main__':
    solution = Solution()
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]

    solution.merge_better(arr1, 3, arr2, 3)
    print(arr1)