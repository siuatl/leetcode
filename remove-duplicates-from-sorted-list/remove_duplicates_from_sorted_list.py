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


def print_linked_list(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next


def deleteDuplicates(head):
    # class Solution:
    node = head
    while node != None:
        while node.next != None and node.next.val == node.val:
            node.next = node.next.next
        node = node.next
    return head


linked_list = link_lis([1, 1, 2])
# print_linked_list(linked_list)
print_linked_list(deleteDuplicates(linked_list))

linked_list = link_lis([1, 1, 2, 3, 3])
# print_linked_list(linked_list)
print_linked_list(deleteDuplicates(linked_list))

linked_list = link_lis([1, 1, 1, 1, 1])
# print_linked_list(linked_list)
print_linked_list(deleteDuplicates(linked_list))
