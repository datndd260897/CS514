def bubbledown(heap, i):
    n = len(heap)
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Find the smallest among root, left child and right child
    if left < n and heap[left] < heap[smallest]:
        smallest = left
    if right < n and heap[right] < heap[smallest]:
        smallest = right

    # If the smallest is not root, swap and continue bubbling down
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        bubbledown(heap, smallest)

def heapify(heap, i=0):
    n = len(heap)
    if 2 * i + 1 >= n:  # leaf node?
        return
    heapify(heap, 2 * i + 1)  # heapify left subtree
    heapify(heap, 2 * i + 2)  # heapify right subtree
    bubbledown(heap, i)  # adjust root

# Example usage
arr = [9, 5, 6, 2, 3]

print("Before heapify:", arr)
heapify(arr)
print("After heapify (min-heap):", arr)
