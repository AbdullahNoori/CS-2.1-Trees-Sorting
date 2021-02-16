#!python


def merge(nlist):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # # TODO: Append remaining items in non-empty list to new list

    # left_index, right_index = 0, 0
    # result = []
    # while left_index < len(left) and right_index < len(right):
    #     if left[left_index] < right[right_index]:
    #         result.append(left[left_index])
    #         left_index += 1
    #     else:
    #         result.append(right[right_index])
    #         right_index += 1

    # result += left[left_index:]
    # result += right[right_index:]
    # return result


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    if len(items)>1:
        mid = len(items)//2
        left_half = items[:mid]
        right_half = items[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0       
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                items[k]=left_half[i]
                i=i+1
            else:
                items[k]=right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):
            items[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):
            items[k]=right_half[j]
            j=j+1
            k=k+1
    print("Merging ",items)

items = [14,46,43,27,57,41,45,21,70]
merge_sort(items)
print(items)




        
            

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort







# 1. create two sorted lists 
 # Get the length of both lists
# iterate through both lists until you reach the end of both them 





#  TIme complexity is 0(n log n)


# if len(items) > 1:  
#         mid = len(items)//2

#         first_half = items[:mid]

#         second_half = items[mid:]

#         # Sorting the first half
#         merge_sort(first_half)
#         # Sorting the first half
#         merge_sort(second_half)

#         x = y = z = 0
#     # Copies the date to temp arrays first_half[] and second_half[]
#         while x < len(first_half) and y < len(second_half):    
#             if first_half[x] < second_half[y]: 
#                 items[z] = first_half[x]
#                 x += 1
#             else:   
#                 items[z] = second_half[y]
#                 z += 1

#     # Checks to see if any elements are left out.    
#         while x < len(first_half):
#             items[z] = second_half(x)
#             x += 1
#             z += 1
        
#         while y < len(second_half):
#             items[z] = second_half[y]
#             y += 1
#             z += 1
