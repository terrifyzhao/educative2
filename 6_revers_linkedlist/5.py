from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, rotations):
    length = 1
    cur = head

    while cur.next:
        cur = cur.next
        length += 1
    cur.next = head

    k = length - rotations % length

    i = 0
    cur = head
    while cur and i < k:
        cur = cur.next
        i += 1
    head = cur.next
    cur.next = None
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 8)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
