
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def sorted_merge(head1, head2):
    # Base case
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val < head2.val:
        head1.next = sorted_merge(head1.next, head2)
        return head1
    else:
        head2.next = sorted_merge(head1, head2.next)
        return head2

