# [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

## 问题

从 `m` 到 `n` 的位置反转链表。找一种 one-pass 解决方案。

`1 <= m <= n <= len(List)`。

**例子：**

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

## 思路

这个题目其实是 based on 第 206 题的。无论是是递归法还是迭代法，我们都需要 figure out some points。

1. 首先，我们需要遍历节点到反转部分启始点，并保存其前一个节点用于连接。
2. 反转需要反转的部分。
3. 在反转部分结束点停止，并将反转部分与后面部分连接。

Talk is cheap, let's see the code!

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head or not head.next: return head
        
        head, head.next = ListNode(None), head
        node = head
        for i in range(m - 1):
            node = node.next
            
        prev, tail, h = None, node.next, node.next
        for i in range(m, n + 1):
            curr = h
            h = h.next
            curr.next = prev
            prev = curr
        
        node.next = prev
        tail.next = h
        
        return head.next
```