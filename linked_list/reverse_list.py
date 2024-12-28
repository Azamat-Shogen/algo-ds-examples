
# Recursive
def reverse_list(head):
    if head is None or head.next is None:
        return head

    p = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p
