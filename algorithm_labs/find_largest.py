from typing import List

def recursion_largest(my_list:List):
    if len(my_list) == 0:
        raise ValueError('list must not be empty')
    elif len(my_list) == 1:
        return my_list[0]
    else:
        largest = recursion_largest(my_list[1:])
        return largest if largest > my_list[0] else my_list[0]

def sequential_largest(my_list:List):
    if len(my_list) == 0:
        raise ValueError('list must not be empty')
    elif len(my_list) == 1:
        return my_list[0]
    else:
        largest = my_list[0]
        for element in my_list:
            if element > largest:
                largest = element
        return largest



if __name__ == '__main__':
    my_list = [1,2,32,4,5,6]

    print(sequential_largest(my_list))
    print(recursion_largest(my_list))