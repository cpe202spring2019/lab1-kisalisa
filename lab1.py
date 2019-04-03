
def max_list_iter(int_list):  # must use iteration not recursion
    try: 
        int_list[0]
    except:
        raise ValueError
        return None
    biggest = int_list[0]
    for num in int_list:
        if num > biggest:
            biggest = num
    return biggest

def reverse_rec(int_list):   # must use recursion
    try:
        int_list[0]
    except:
        raise ValueError
        return None
    if len(int_list) == 1:
        return int_list
    else:
        return int_list[] + reverse_rec(int_list) 

    # not recursion below... change this
    '''
    try:
        int_list[0]
    except:
        raise ValueError
        return None
    return int_list[::-1]        
    '''

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
