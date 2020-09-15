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


def reverse_alternate_k_elements(head, k):
    pre, cur = None, head
    while 1:

        first, second = pre, cur
        i = 0
        while cur and i < k:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            i += 1

        if first is not None:
            first.next = pre
        else:
            head = pre
        second.next = cur
        pre = second

        i = 0
        while cur and i < k:
            pre = cur
            cur = cur.next
            i += 1
        if cur is None:
            break

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
