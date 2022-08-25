# an algorithm that finds the m smallest numbers in a list of n numbers
from typing import List


def m_smallest_numbers(my_list:List, m:int):
    for i in range(len(my_list)):
        smallest_index = i
        for j in range(i,len(my_list)):
            if my_list[j] < my_list[smallest_index]:
                smallest_index = j
        my_list[i], my_list[smallest_index] = my_list[smallest_index], my_list[i]
    return my_list[:m]

def m_smallest_numbers_solution2(my_list:List, m:int):
    temp = []
    for i in range(m):
        min_index = 0
        for j in range(len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        temp.append(my_list[min_index])
        my_list[0], my_list[min_index] = my_list[min_index], my_list[0]
        my_list = my_list[1:]
    return temp


if __name__ == '__main__':
    my_list = [1, 4, 2, 6, 3, 6, 2, 4, 6, 1]
    #print(m_smallest_numbers(my_list, 5))
    print(m_smallest_numbers_solution2([1, 4, 2, 6, 3, 6, 2, 4, 6, 1], 5))