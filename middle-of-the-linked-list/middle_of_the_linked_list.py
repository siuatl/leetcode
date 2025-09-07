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


def print_linked_list(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next


def middleNode(head):
    # class Solution:
    node = head
    node_2 = head
    while node_2 != None and node_2.next != None:
        node = node.next
        node_2 = node_2.next.next
    return node


list_or = link_lis([1, 2, 3, 4, 5])
print_linked_list(middleNode(list_or))

# list_or = link_lis([1, 2, 3, 4, 5, 6])
# print_linked_list(middleNode(list_or))

# list_or = link_lis([1, 2, 3, 4])
# print_linked_list(middleNode(list_or))


# list_or = link_lis([1, 2, 3, 4, 5, 6, 7])
# print_linked_list(middleNode(list_or))
