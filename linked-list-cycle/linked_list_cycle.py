# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def link_lis_cycl(org_list):
    # Building linked list.
    head = ListNode(org_list[0])
    node = head

    for elem in org_list[1:]:
        node.next = ListNode(elem)
        node = node.next
    return head


def hasCycle(head):
    node = head
    node2 = head
    while node != None and node2 != None:
        if node2.next == None:
            return False
        node = node.next
        node2 = node2.next.next
        if node == node2:
            return True
    return False


lis_t = link_lis_cycl([3, 2, 0, -4])
lis_t.next.next.next.next = lis_t.next
print(hasCycle(lis_t))


# def hasCycle(head):
#     nodes_seen = set()
#     node = head
#     while node != None:
#         if node in nodes_seen:
#             return True
#         nodes_seen.add(node)
#         node = node.next
#     return False
