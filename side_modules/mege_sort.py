
from typing import List


def merge_sort(num_list) -> None:
    if len(num_list) > 1:
        # separating first
        mid = len(num_list) // 2

        left_list = num_list[:mid]
        right_list = num_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = 0
        j = 0
        k = 0

        # comparing and inserting into the original list
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                num_list[k] = left_list[i]
                i += 1
            else:
                num_list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            num_list[k] = left_list[i]
            k += 1
            i += 1

        while j < len(right_list):
            num_list[k] = right_list[j]
            k += 1
            j += 1


if __name__ == '__main__':
    num_list=[33,6,788,11,2,5,909,99,12]
    merge_sort(num_list)
    print(num_list)