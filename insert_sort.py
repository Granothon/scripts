'''Insertion Sort Algorithm for arrays where the data is nearly sorted or the size of array is small'''
def insert_sort(lst: list):
    n = 1 # second item
    while n < len(lst):
        pivot = lst[n]
        m = n
        while m - 1 >= 0 and lst[m - 1] > pivot:
            lst[m] = lst[m - 1]
            lst[m - 1] = pivot
            m -= 1
        n += 1

# test cases        
lista = ["gabriel", "aapeli", "jellona", "booli", "karhu", "coca-cola", "kassinen", "laite", "lomamatka"]
print (f"unsorted: {lista}")
insert_sort(lista)
print (f"sorted: {lista}")