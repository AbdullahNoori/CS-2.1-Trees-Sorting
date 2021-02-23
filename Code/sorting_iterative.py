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


