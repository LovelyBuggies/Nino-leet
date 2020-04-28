# [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

## 问题

将链表中所有值为 `val` 的节点从链表中移除。

**例子：**

```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

## 思路

链表基操，无需赘言。值得注意的是，开头设置要一个 dummy node 来进行头移除；以及进行值比较的时候用的是 `node.next`（*因为如果要移除一个节点，必须从它的前一个节点开始*）。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        head, head.next = ListNode(None), head
        node = head
        while node.next:
            if node.next.val == val: node.next = node.next.next
            else: node = node.next
                
        return head.next
```