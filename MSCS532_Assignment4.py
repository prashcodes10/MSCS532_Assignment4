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
