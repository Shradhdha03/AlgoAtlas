## **Remove Duplicates from a Sorted Linked List**

### **Problem Statement:**

Given the head of a sorted linked list, the task is to delete all duplicates such that each element appears only once. The resulting linked list should be returned sorted as well.

### **Constraints:**

- The number of nodes in the list is in the range [0, 300].
- Node values range from -100 to 100.
- The list is guaranteed to be sorted in ascending order.

### **Test Cases:**

1. **Input**: head = [1,1,2]  
   **Output**: [1,2]

2. **Input**: head = [1,1,2,3,3]  
   **Output**: [1,2,3]

### **My Solution Explanation:**

The solution provided is an iterative method (`deleteDuplicates`) and a recursive method (`deleteDuplicatesRecursive`) to delete duplicates from a sorted linked list:

- **Iterative Method**: 
    1. If the head doesn't exist, return `None`.
    2. Initialize two pointers, `prev` (pointing to the head) and `current` (pointing to the next node).
    3. Iterate through the list. If the value of the `current` node is the same as the `prev` node, skip the `current` node by updating the next of `prev`.
    4. If the values are different, move both pointers to the next node.
    5. Repeat this process until the end of the list.

- **Recursive Method**: 
    1. If the head doesn't exist, return `None`.
    2. Recursively call the `deleteDuplicatesRecursive` method for the next node of the head.
    3. If the value of the current node is the same as its next node, skip the current node.
    4. If the values are different, return the current node.

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return None if head doesn't exist
        if not head:
            return None
        
        # Take two pointers, prev and current
        prev, current = head, head.next
        
        # Iterate through the list till the end
        while current:
            # If the value of current and previous is the same, skip the current
            if current.val == prev.val:
                prev.next = current.next
            else:
                prev = current 
            current = current.next
        
        return head

    def deleteDuplicatesRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return None if head doesn't exist
        if not head:
            return None
        
        head.next = self.deleteDuplicatesRecursive(head.next)
        
        if head.next and head.val == head.next.val:
            return head.next
        else:
            return head

```

### **Complexity Analysis:**

- **Iterative Method (`deleteDuplicates`)**:
    - **Time Complexity**: The method iterates through the list once. Therefore, the time complexity is \(O(n)\), where \(n\) is the number of nodes in the list.
    - **Space Complexity**: Since we're using only a constant amount of extra space (two pointers), the space complexity is \(O(1)\).

- **Recursive Method (`deleteDuplicatesRecursive`)**:
    - **Time Complexity**: Like the iterative method, this method processes each node once, resulting in a time complexity of \(O(n)\).
    - **Space Complexity**: Due to the recursive calls, the space complexity is \(O(n)\) in the worst case, which happens due to the call stack.

### **Technical Follow-up Questions (with answers):**

1. **Question**: How would you handle removing duplicates if the linked list contains billions of nodes?
    - **Answer**: For very large datasets, we might consider using a distributed system or parallel processing to handle the data. Also, using an iterative approach would be more memory-efficient than a recursive approach due to the call stack limitations.

2. **Question**: How would you ensure the scalability of your solution for huge linked lists?
    - **Answer**: Using techniques like sharding (breaking data into smaller, more manageable pieces) and parallel processing can ensure scalability. Further, employing algorithms that work efficiently with streaming data can be beneficial.

3. **Question**: How would you handle cases where there is not enough memory to load the entire linked list?
    - **Answer**: One approach could be using external sorting, where data is divided into chunks small enough to be sorted in memory and then merged.

### **Real-world use cases:**

1. **Database Systems**: When retrieving data from a database, often, we need to remove duplicates. This problem mimics that scenario but in the context of linked lists.
   
2. **Contacts Management**: In applications managing contacts or emails, there might be duplicate entries that need to be removed.

3. **Inventory Management**: In systems that manage inventory or stock, ensuring there are no duplicate entries is crucial for accurate tracking.

4. **Data Cleansing**: In any real-world scenario where data integrity is essential, removing duplicates is a fundamental step in the process of data cleansing.