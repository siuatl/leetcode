# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def link_lis(org_list):
    # Building linked list.
    head = ListNode(org_list[0])
    node = head

    for elem in org_list[1:]:
        node.next = ListNode(elem)
        node = node.next
    return head


def reverseList(head):
    # class Solution:
    prev = None
    current = head
    while current != None:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev


def print_linked_list(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next


linked_list = link_lis([1, 2, 3, 4, 5])
print_linked_list(reverseList(linked_list))
