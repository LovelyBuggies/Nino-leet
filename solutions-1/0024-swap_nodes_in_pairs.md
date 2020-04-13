# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

## 问题

给定一个链表，要求每两个节点交换一下位置。

你**不能**修改节点的val，只有节点本身可以被交换。

**例子：**

``
Input: 1->2->3->4
Output: 2->1->4->3
```

## 思路

这个题目其实不是很难，就是交换两个节点位置，并指向后续第三个节点。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head and head.next:
            tmp1, tmp2 = head, head.next.next
            head = head.next
            head.next = tmp1
            head.next.next = self.swapPairs(tmp2)
            return head
        else: return head
```

