# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        count = 0
        node1 = head
        while node1:
            count += 1
            node1 = node1.next
        bit = 0 
        sum = count - 1
        while head:
            # print(node.val)
            bit += 2**sum * head.val
            sum -= 1
            head = head.next
        return bit
    
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

head = create_linked_list([1,0,1])
solution = Solution()
print(solution.getDecimalValue(head))