class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def is_palindromic_linked_list(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    tail = reverse(slow)
    copy_tail = tail

    while head and tail:
        if head.value != tail.value:
            return False
        head = head.next
        tail = tail.next

    reverse(copy_tail)

    return True


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
