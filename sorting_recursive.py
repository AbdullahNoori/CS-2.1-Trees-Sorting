#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) > 1:  
        mid = len(items)//2

        first_half = items[:mid]

        second_half = items[mid:]

        # Sorting the first half
        merge_sort(first_half)
        # Sorting the first half
        merge_sort(second_half)

        x = y = z = 0
# Copies the date to temp arrays first_half[] and second_half[]
        while x < len(first_half) and y < len(second_half):    
            if first_half[x] < second_half[y]: 
                items[z] = first_half[x]
                x += 1
            else:   
                items[z] = second_half[y]
            z += 1

                # Checks to see if any elements are left out.    
        while x < len(first_half):
            items[z] = second_half(x)
            x += 1
            z += 1
        
        while y < len(second_half):
            items[z] = second_half[y]
            y += 1
            z += 1

# Prints the list of items
def printList(items):      
    for x in range(len(items)): 
        print(items[x], end=" ")
    print()

if __name__ == '__main__':  
    items = [100, 5, 1, 20, 30, 40, 80, 100, 30, 40]
    print("The Given array is", end="\n")
    print(items)
    merge_sort(items)
    print("the Sorted array is: ", end="\n")
    print(items)
        
            

# def partition(items, low, high):
#     """Return index `p` after in-place partitioning given items in range
#     `[low...high]` by choosing a pivot (TODO: document your method here) from
#     that range, moving pivot into index `p`, items less than pivot into range
#     `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Choose a pivot any way and document your method in docstring above
#     # TODO: Loop through all items in range [low...high]
#     # TODO: Move items less than pivot into front of range [low...p-1]
#     # TODO: Move items greater than pivot into back of range [p+1...high]
#     # TODO: Move pivot item into final position [p] and return index p


# def quick_sort(items, low=None, high=None):
#     """Sort given items in place by partitioning items in range `[low...high]`
#     around a pivot item and recursively sorting each remaining sublist range.
#     TODO: Best case running time: ??? Why and under what conditions?
#     TODO: Worst case running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Check if high and low range bounds have default values (not given)
#     # TODO: Check if list or range is so small it's already sorted (base case)
#     # TODO: Partition items in-place around a pivot and get index of pivot
#     # TODO: Sort each sublist range by recursively calling quick sort
