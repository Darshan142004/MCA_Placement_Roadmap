class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None

# Empty list

print(detectCycle(None))

#  Single node, no cycle

node = ListNode(1)
print(detectCycle(node))

#  Single node with cycle

node.next = node
print(detectCycle(node).val)

# Multiple nodes with cycle
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(detectCycle(node1).val)
