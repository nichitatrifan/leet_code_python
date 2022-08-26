from typing import List


def insertion_binary_sort(my_list:List):
    end = 0
    start = 0
    for i in range(end+1, len(my_list)):
        found = False
        while not found:
            if start == end:
                my_list[start], my_list[i] = my_list[i], my_list[start]
                found = True
            middle = (start + end) // 2
            if my_list[middle] > my_list[i]:
               end = middle - 1
            elif not found:
                start = middle + 1
        end += 1
        start = 0

if __name__ == '__main__':
    my_list = [6,1,2,7,3]
    insertion_binary_sort(my_list)
    print(my_list)