# [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## 问题

给定一个链表，去除重复元素，保证每个元素最多出现一次。

**例子：**

```
Input: 1->1->2
Output: 1->2

Input: 1->1->2->3->3
Output: 1->2->3
```

## 思路

这个题目不算难，遍历链表去重复就好了，属于链表的基本操作。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head: return head
        
        node = head
        while node.next:
            if node.val == node.next.val: node.next = node.next.next
            else: node = node.next
                
        return head
```
