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


def getDecimalValue(head) -> int:
    # class Solution:
    current_num = 0
    node = head
    while node != None:
        current_num = current_num << 1
        current_num += node.val
        node = node.next
    return current_num


linked_list = link_lis([1, 0, 1])
print(getDecimalValue(linked_list))


# # OPTION 2
# def getDecimalValue2(head) -> int:
#     str_binary = ""
#     node = head
#     while node != None:
#         str_binary += str(node.val)
#         node = node.next
#     return int(str_binary, 2)
