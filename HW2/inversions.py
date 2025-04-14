def merge_count_split_inv(left, right):
    result = []
    i = j = 0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            # All remaining elements in left are greater than right[j]
            inv_count += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_count

def sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = sort_count(arr[:mid])
    right, inv_right = sort_count(arr[mid:])
    merged, inv_split = merge_count_split_inv(left, right)
    return merged, inv_left + inv_right + inv_split

def num_inversions(arr):
    _, count = sort_count(arr)
    return count

if __name__ == '__main__':
    print(num_inversions([4, 1, 3, 2]))
    print(num_inversions([2, 4, 1, 3]))
