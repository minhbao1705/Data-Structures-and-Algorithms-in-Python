from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]

        # Intialize minimum distance to the maximum possible value
        min_distance = float("inf")

        # Pointers to track the previous node, current node, and indices
        previous_node = head
        current_node = head.next
        current_index = 1 
        previous_critical_index = 0
        first_critical_index = 0
        
        while current_node.next is not None:
            if (current_node.val < previous_node.val
                and current_node.val < current_node.next.val
            ) or (current_node.val > previous_node.val
                and current_node.val > current_node.next.val):
                if previous_critical_index == 0:
                    previous_critical_index = current_index
                    first_critical_index = current_index
                else:
                    min_distance = min(min_distance, current_index - previous_critical_index)
                    previous_critical_index = current_index
            
            current_index += 1
            previous_node = current_node
            current_node = current_node.next
            
            if min_distance != float("inf"):
                max_distance = previous_critical_index - first_critical_index
                result = [min_distance, max_distance]
                
        return result

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

head =create_linked_list([5,3,1,2,5,1,2])
solution = Solution()
print(solution.nodesBetweenCriticalPoints(head))