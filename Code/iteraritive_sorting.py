# #!python
# import time

# def is_sorted(items):
#     """Return a boolean indicating whether given items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Check that all adjacent items are in order, return early if so
#     if len(items) == 0:
#         return True
    
#     prev = items[0]
#     for i in range(1, len(items)):   # O(n)
#         if prev > items[i]:          # O(1)
#             return False
#         prev = items[i]
#     return True


# def bubble_sort(items):
#     """Sort given items by swapping adjacent items that are out of order, and
#     repeating until all items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Swap adjacent items that are out of order
#     num_items = len(items)
#     # loop over items from 0 to length of items
#     for i in range(num_items-1):                        
#         # loop over items from 0 to i minus 1 for comparing
#         for j in range(0, num_items-i-1):
#             # check if second to last item is greater than last item
#             if items[j] > items[j+1]:
#                 # swapping
#                 (items[j], items[j+1]) = (items[j+1], items[j])
                
#     return items

# def selection_sort(items):
#     """Sort given items by finding minimum item, swapping it with first
#     unsorted item, and repeating until all items are in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # TODO: Find minimum item in unsorted items
#     # TODO: Swap it with first unsorted item
#     num = len(items)
    
#     for i in range(num):                    # O(n^2)
#         for j in range(i, num):
#             if items[i] > items[j]:
#                 (items[i], items[j]) = (items[j], items[i])
                
#     return items

# def insertion_sort(items):
#     """Sort given items by taking first unsorted item, inserting it in sorted
#     order in front of items, and repeating until all items are in order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until all items are in sorted order
#     # [10, 6, 8, 2, 100, 23]
#     num = len(items)
    
#     for i in range(1, num):
#         value = items[i]
#         j = i - 1
#         while j >= 0:
#             if items[i] < items[j]:
#                 items[j+1] = items[j]
#                 items[j] = value
#                 j -= 1
#             else:
#                 break
        
#     return items
    
    
    
# if __name__ == '__main__':
#     sorted_items = [0, 1, 2, 4, 5]
#     unsorted_items = [10, 5, 3, 7, 100, -100]
#     print("Sorted items list1: {}".format(sorted_items))
#     print("Unsorted items list2: {}".format(unsorted_items))
    
#     print("is list1 sorted: {}".format(is_sorted(sorted_items)))
#     print("is list2 sorted: {}".format(is_sorted(unsorted_items)))
    
#     bubbleSort1 = bubble_sort(sorted_items)
#     bubbleSort2 = bubble_sort(unsorted_items)
#     print("Bubble sort list1: {}".format(bubbleSort1))
#     print("Bubble sort list2: {}".format(bubbleSort2))
    
#     selection_sort1 = selection_sort(sorted_items)
#     selection_sort2 = selection_sort(unsorted_items)
#     print("Selection sort list1: {}".format(selection_sort1))
#     print("Selection sort list2: {}".format(selection_sort2))
    
#     insertion_sort1 = insertion_sort(sorted_items)
#     insertion_sort2 = insertion_sort(unsorted_items)
#     print("Insertion sort list1: {}".format(insertion_sort1))
#     print("Insertion sort list2: {}".format(insertion_sort2))
    
#     start = time.time()
#     result = is_sorted(sorted_items)
#     end = time.time()
#     print(sorted_items)
#     print("Sorted: {}. Time: {}\n".format(result, (end-start)))
    

#     start = time.time()
#     result = is_sorted(unsorted_items)
#     end = time.time()
#     print(unsorted_items)
#     print("Sorted: {}. Time: {}".format(result, (end-start)))










    #!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so

    items = [11,23,42,51,67, 99, 100]
    #Given list
    print("Given list : ",items)
    # Apply all and range
    if (all(items[i] <= items[i + 1] for i in range(len(items)-1))):
    print("Yes, List is sorted.")
    else:
    print("No, List is not sorted.")


    # Checking again
    itemsB = [51, 11,23,42,67,100,99]
    print("Given list : ",items)
    # Apply all and range
    if (all(itemsB[i] <= itemsB[i + 1] for i in range(len(itemsB)-1))):
    print("Yes, List is sorted.")
    else:
print("No, List is not sorted.")

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    list = len(items)
    #Traverse throug all array elemts 
    for a in range(len(items)-1, 0, -1):
    #Last I elements are a lreay in correct position 
        for  i in range(a):
            #Swap if the element found is greater than the next element 
            if items[i] > items[i + 1] :
                swap = items[i]
                items[i] = items[i + 1]
                items[i+1] = swap


items = ['a', 'f', 'g', 'z', 'b', 'i', 'k', 'c']
bubble_sort(items)
print ("Your sorted array is:", items)
    # print(bubble_sort(items))

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    index_length = range(0, len(items)-1)

    for i in index_length:
        min_value = i

        for j in range(i+1, len(items)):
            if items[j] < items[min_value]:
                min_value = j

        if min_value != i:
            items[min_value], items[i] = items[i], items[min_value]

    return items

print(selection_sort([1, 8, 22, 45, 9, 47, 20, 40, 80])) 



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    index_length = range(1, len(items))
    for i in index_length:
        sort_to_value = items[i]

        while  items[i-1] > sort_to_value and i>0:
            items[i], items[i-1] = items[i-1], items[i]
            i-=1

    return items


print(insertion_sort([5, 12, 3, 2, 10, 24, 1, 8, 20]))


