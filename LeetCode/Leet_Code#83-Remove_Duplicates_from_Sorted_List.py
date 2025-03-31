from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
    
# Hàm in danh sách liên kết
def print_linked_list(head: Optional[ListNode]):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

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

head = create_linked_list([1,1,2,3,3])
solution = Solution()
new_list = solution.deleteDuplicates(head)

print_linked_list(new_list)  # Corrected line