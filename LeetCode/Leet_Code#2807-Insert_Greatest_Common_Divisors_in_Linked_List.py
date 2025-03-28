from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        node1 = head
        while node1.next:
            node2 = node1.next
            gcd_value = gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)
            node1.next = gcd_node
            gcd_node.next = node2
            node1 = node2
        
        return head

# Hàm in danh sách liên kết
def print_linked_list(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)  # In ra danh sách các giá trị

# Tạo danh sách liên kết từ mảng
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Chạy thử
head = create_linked_list([18, 6, 10, 3])
solution = Solution()
new_head = solution.insertGreatestCommonDivisors(head)

print_linked_list(new_head)  # In kết quả ra VS Code terminal
