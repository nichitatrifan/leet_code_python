from typing import List


def n_sorting(my_list:List, k:int):
    buffer_list: List[int] = [] # should be the size of 'k*n'
    return_list: List[int] = [] # should be the size of 'n'

    for i in range(0,k*len(my_list)):
        buffer_list.append(0)

    for i in range(0,len(my_list)):
        buffer_list[my_list[i]] = 1

    k = 0
    for i in range(0, len(buffer_list)):
        if buffer_list[i] == 1:
            return_list.append(i)
            k += 1

    return return_list

if __name__ == '__main__':
    print(n_sorting([10,55,1,23,43,5,20], 9))