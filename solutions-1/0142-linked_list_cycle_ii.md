# [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## 问题

给定一个链表，判断它是否有一个循环。

为了在给定的链表中表示一个循环，我们使用一个整数 `pos` 来表示链表尾连接到的链表中的位置。如果 `pos` 是 -1，那么链表中就没有循环。

**例子：**

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)



```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)



```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)



**跟进：**

你可以用常数内存实现么？

## 思路

判断一个链表是否循环可以用一个有用的性质：如果链表中有循环，那么一个步长为 2 的快指针会在某一刻遇到步长为 1 的慢指针，且套它一圈。***至于在何处相遇嘛，这个不确定 :) 但我们还是可以求出来的何处相遇的，详见第 142 题。***

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def hasCycle(self, head: ListNode) -> bool:
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        
        return False
```