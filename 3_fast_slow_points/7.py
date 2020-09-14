# 题目要求不能只有一个元素，不能存在两个方向
def next_index(arr, index, is_forward):
    direction = arr[index] >= 0
    if direction != is_forward:
        return -1

    next_index = (index + arr[index]) % len(arr)
    if next_index == index:
        return -1
    return next_index


def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow = i
        fast = i
        while 1:
            slow = next_index(arr, slow, is_forward)
            fast = next_index(arr, fast, is_forward)
            if fast != -1:
                fast = next_index(arr, fast, is_forward)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    return False


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
