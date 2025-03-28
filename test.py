class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list = [18,6,10,3]
head = ListNode()
for l in list:
    while head.next:
        head = head.next
    head = ListNode(l,None)
print(head.val)