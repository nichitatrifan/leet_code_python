from typing import List


def print_subsets(my_list:List):
    if len(my_list) < 3:
        raise ValueError('List size is too small!')

    for i in range(0, len(my_list)-2):
        for j in range(i+1, len(my_list)-1):
            for k in range(j+1, len(my_list)):
                print(str(my_list[i]) + ' ' + str(my_list[j]) + ' ' + str(my_list[k]))

if __name__ == '__main__':
    print_subsets([10, 20, 30, 40, 50])