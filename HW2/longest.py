def depth(t):
    if t == []:
        return 0, -1  # (longest_path, height)

    left, _, right = t
    longest_left, height_left = depth(left)
    longest_right, height_right = depth(right)

    height = max(height_left, height_right) + 1
    path_through_node = height_left + height_right + 2
    longest_path = max(longest_left, longest_right, path_through_node)

    return longest_path, height

def longest(t):
    longest_path, _ = depth(t)
    return longest_path

if __name__ == '__main__':
    print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))
    print(longest([[[], 1, []], 2, [[], 3, []]]))
    print(longest([[], 1, []]))