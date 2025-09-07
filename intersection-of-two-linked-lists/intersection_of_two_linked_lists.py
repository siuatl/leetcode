# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def link_lis(org_list):
    # Building linked list.
    head = ListNode(org_list[0])
    node = head

    for elem in org_list[1:]:
        node.next = ListNode(elem)
        node = node.next
    return head


def getIntersectionNode(headA, headB):
    seen_a = set()
    node_a = headA
    while node_a != None:
        if node_a in seen_a:
            break
        seen_a.add(node_a)
        node_a = node_a.next

    seen_b = set()
    node_b = headB
    while node_b != None:
        if node_b in seen_a:
            return node_b.val
            # return f"Intersected at {node_b.val}"
        if node_b in seen_b:
            break
        seen_b.add(node_b)
        node_b = node_b.next
    return "No intersection"


head_a = link_lis([4, 1, 8, 4, 5])
head_b = link_lis([5, 6, 1])
head_b.next.next.next = head_a.next.next
print(getIntersectionNode(head_a, head_b))


head_a = link_lis([4, 1, 8, 4, 5])
head_b = link_lis([5, 6, 1, 6])
print(getIntersectionNode(head_a, head_b))

head_a = link_lis([1, 9, 1, 2, 4])
head_b = link_lis([3, 2, 4])
head_b.next.next = head_a.next.next.next
print(getIntersectionNode(head_a, head_b))
