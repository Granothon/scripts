'''Binary search algorithm. Needs a sorted list to function properly'''

def bin_search(lst: list, target):
    n = len(lst)
    
    # Check if list is empty
    if n == 0:
        return False
    
    # Do the search
    pivot = lst[n // 2]
    if target == pivot:
        return True
    
    # Split the list and recurse
    elif target < pivot:
        part = lst[:n // 2]
        return bin_search(part, target)

    elif target > pivot:
        part = lst[n // 2 + 1:]
        return bin_search(part, target)

# Test cases
lista = [11, 12, 15, 30, 50, 83, 90, 110, 117]
query_list = [21, 83, 99, 117] # False, True, False, True

for query in query_list:
    print(bin_search(lista, query))