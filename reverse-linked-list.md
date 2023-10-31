
### Reverse Linked List

#### Problem Statement:
Given the head of a singly linked list, the task is to reverse the linked list and return the reversed list.

#### Constraints:
- The number of nodes in the list lies in the range [0, 5000].
- The value of each node lies in the range [-5000, 5000].

#### Test Cases:
1. Input: `head = [1,2,3,4,5]`  
   Output: `[5,4,3,2,1]`

2. Input: `head = [1,2]`  
   Output: `[2,1]`

3. Input: `head = []`  
   Output: `[]`

#### My Solution Explanation:
The linked list can be reversed using multiple approaches. I have implemented the following three methods:

1. **Iterative Method**: This method reverses the list in-place by adjusting the pointers of each node.
2. **Using a New List**: This approach creates a new list with reversed nodes.
3. **Recursive Method**: This solution recursively reverses the sublist and then adjusts the pointers.

```python   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse the linked list in place.

        Args:
        - head (ListNode): The head of the linked list.

        Returns:
        - ListNode: The head of the reversed linked list.
        """
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next  # Store next node
            current_node.next = prev_node  # Reverse current node's pointer
            prev_node = current_node  # Move to next node
            current_node = next_node

        return prev_node

    def reverseListNewList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Create a new reversed linked list based on the input linked list.

        Args:
        - head (ListNode): The head of the linked list.

        Returns:
        - ListNode: The head of the new reversed linked list.
        """
        new_list_head = None

        while head:
            # Create a new node with the current value
            new_node = ListNode(head.val)
            
            # Make the new node point to the current head of the new list
            new_node.next = new_list_head
            
            # Update the head of the new list
            new_list_head = new_node
            
            # Move to the next node in the input list
            head = head.next

        return new_list_head

   def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If head is None or there's only one node, return the head
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list
        reversed_list = self.reverseListRecursive(head.next)
        
        # Adjust pointers
        # 4->5->none
        head.next.next = head
        # 4->5-> back to 4->5-> in cycle
        head.next = None
        # 5->4->None
        
        return reversed_list
```

#### Complexity Analysis:

1. **Iterative Method**:
   - Time Complexity: O(n) - We traverse the list only once.
   - Space Complexity: O(1) - We only use a constant amount of extra space.

2. **Using a New List**:
   - Time Complexity: O(n) - The entire list is traversed once.
   - Space Complexity: O(n) - A new node is created for each element in the original list.

3. **Recursive Method**:
   - Time Complexity: O(n) - Each node is visited once.
   - Space Complexity: O(n) - The recursion stack will hold n elements in the worst case.

#### Technical Follow-up Questions with answers:

1. **How can the iterative solution be optimized if the input linked list contains millions of nodes?**
   - Answer: The provided iterative solution is already optimized in terms of time complexity. For very large datasets, ensuring that the linked list is stored in contiguous memory locations might help improve cache performance. However, this isn't always feasible for linked lists.

2. **If the linked list were doubly linked, how would your solution change?**
   - Answer: For a doubly linked list, another pointer adjustment would be needed for the 'previous' pointer. The basic logic remains the same, but we'd also reverse the back-pointers of each node.

3. **Can the recursive solution handle very large linked lists?**
   - Answer: Recursive solutions are generally limited by the call stack size. For very large linked lists, the recursive solution might lead to a stack overflow. In such cases, an iterative approach is more suitable.

#### Real-world use cases:

1. **Undo Functionality**: Many software applications, like word processors or graphic design tools, maintain a history of actions. To undo an action, they reverse the state. Although not directly related to linked lists, the idea of reversal is used here.
2. **Backtracking Algorithms**: In problems like the "Eight Queens" puzzle, when a solution isn't possible, we backtrack (or 'reverse') to a previous state and continue.
3. **Data Recovery Systems**: Sometimes, systems store changes (or deltas) instead of entire snapshots. To recover a certain state, they might need to reverse through the changes.

