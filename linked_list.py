from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Easy
def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current_node = head
    prev_node = None

    while current_node:
        # current_node.next, prev_node, current_node = prev_node, current_node, current_node.next

        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    head = prev_node
    return head


def merge_two_lists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    head = ListNode()
    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 or list2
    return head.next


def has_cycle(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
