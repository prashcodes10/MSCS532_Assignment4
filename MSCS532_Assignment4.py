#Heap_Sort

def maintain_heap(tree, size, root_index):
   
    max_index = root_index         # Assuming root is the largest
    left_child = 2 * root_index + 1   # Calculating left child index
    right_child = 2 * root_index + 2  # Calculating right child index

    # If left child exists and is greater than root
    if left_child < size and tree[left_child] > tree[max_index]:
        max_index = left_child

    # If right child exists and is greater than current largest
    if right_child < size and tree[right_child] > tree[max_index]:
        max_index = right_child

    # If root is not the largest, swap with the largest child
    if max_index != root_index:
        tree[root_index], tree[max_index] = tree[max_index], tree[root_index]
        # Recursively heapify the affected subtree
        maintain_heap(tree, size, max_index)


def heap_sort(data):
   
    length = len(data)

    # Building a max heap from the input list
    for i in range(length // 2 - 1, -1, -1):
        maintain_heap(data, length, i)

    # Repeatedly extracting the maximum and heapify the remaining elements
    for i in range(length - 1, 0, -1):
        # Move current max (root) to the end
        data[0], data[i] = data[i], data[0]
        # Restore max-heap structure on the reduced heap
        maintain_heap(data, i, 0)

    return data


# ----------------------------------------------------------------------------------------------------------------------
# Execution Block
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    numbers = [11, 3, 5, 73, 2, 17]  # Example 
    print("Original list:", numbers)
    sorted_numbers = heap_sort(numbers)
    print("Sorted list:", sorted_numbers)

#Quick_Sort

def run_quick_sort(data):

    if len(data) <= 1:
        return data  

    # Choosing the pivot element, here 1st
    pivot = data[len(data)//2] #uses middle element as pivot
    left_partition = []
    right_partition = []
    equal_elements = []

    # Partitioning the data into three parts
    for element in data:
        if element < pivot:
            left_partition.append(element)
        elif element > pivot:
            right_partition.append(element)
        else:
            equal_elements.append(element)

    # Step 3: Recursively sorting left and right partitions, then combining them all
    sorted_left = run_quick_sort(left_partition)
    sorted_right = run_quick_sort(right_partition)

    return sorted_left + equal_elements + sorted_right

if __name__ == "__main__":
    unsorted_data = [11, 3, 5, 73, 2, 17] 
    print("Original list:", unsorted_data)
    sorted_data = run_quick_sort(unsorted_data)
    print("Sorted list:", sorted_data)

#Merge_Sort

def run_merge_sort(data):

    if len(data) <= 1:
        return data  

    # Splitting the list into two halves
    middle = len(data) // 2
    left_partition = data[:middle]
    right_partition = data[middle:]

    #Recursively sorting both halves
    sorted_left = run_merge_sort(left_partition)
    sorted_right = run_merge_sort(right_partition)

    #Merging the sorted halves into one sorted list
    return combine(sorted_left, sorted_right)


def combine(left_list, right_list):
    
    result = []  # Final merged result
    left_index = 0
    right_index = 0

    #Comparing elements from both lists and adding the smaller one
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            result.append(left_list[left_index])
            left_index += 1
        else:
            result.append(right_list[right_index])
            right_index += 1

    #Changing any remaining elements from left_list
    while left_index < len(left_list):
        result.append(left_list[left_index])
        left_index += 1

    #Changing any remaining elements from right_list
    while right_index < len(right_list):
        result.append(right_list[right_index])
        right_index += 1

    return result

# ----------------------------
# Main Execution Block
# ----------------------------

if __name__ == "__main__":
    unsorted_list = [11, 3, 5, 73, 2, 17] 
    print("Original list:", unsorted_list)
    sorted_list = run_merge_sort(unsorted_list)
    print("Sorted list:", sorted_list)