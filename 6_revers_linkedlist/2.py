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


def reverse_sub_list(head, p, q):
    pre, cur = None, head
    i = 1
    while cur and i < p:
        pre = cur
        cur = cur.next
        i += 1

    first_part_last_node = pre
    second_part_last_node = cur

    while cur and i < q + 1:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        i += 1

    if first_part_last_node:
        first_part_last_node.next = pre
    else:
        head = pre

    second_part_last_node.next = cur
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
