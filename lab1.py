# Name: Lisa Li
# Assignment: Lab 1
# Course: Gaming 202
# Instructor: Paul Hatalsky
# Term: Spring 2019


def max_list_iter(int_list):  # must use iteration not recursion
    if int_list is None:
        raise ValueError
    elif int_list == []:
        return None
    biggest = int_list[0]
    for num in int_list:
        if num > biggest:
            biggest = num
    return biggest


def reverse_rec(int_list):   # must use recursion
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return []   
    elif len(int_list) == 1:
        return int_list
    return [int_list[-1]] + reverse_rec(int_list[:-1]) 
    

def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    if high >= low: 
        mid = (low + high) // 2
        if int_list[mid] == target:
            return mid 
        elif int_list[mid] > target:
            return bin_search(target, low, mid - 1, int_list) 
        else:
            return bin_search(target, mid + 1, high, int_list)
    else: 
        return None
