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


# class Solution:
def removeElements(head, val: int):
    node = head
    while node != None:
        if node.val == val:
            node = node.next
        else:
            break
    head = node
    while node != None:
        while node.next != None and node.next.val == val:
            node.next = node.next.next
        node = node.next
    return head


def print_linked_list(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next


linked_list = link_lis([7, 7, 1])
print_linked_list(removeElements(linked_list, 7))

linked_list = link_lis([7, 7, 7, 7])
print_linked_list(removeElements(linked_list, 7))

linked_list = link_lis([1, 2, 6, 3, 4, 5, 6])
print_linked_list(removeElements(linked_list, 6))
