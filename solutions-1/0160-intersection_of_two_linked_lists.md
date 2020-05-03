# [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

## 问题

写一个程序找到两个链表交汇的地方。

**例子：**

![img](https://assets.leetcode.com/uploads/2018/12/13/160_statement.png)

交汇到了节点 `c1`。



![img](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

交汇到了节点 `8`。



![img](https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png)

交汇到了节点 `2`。



![img](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)

交汇到了节点 None。

**注意：**

- 如果两个节点没有交汇，返回 None。
- 链表不能被更改。
- 没有环出现在整个交汇链表中。
- 试图用线性时间复杂度和常数空间复杂度解决这个问题。

## 思路

一个很直观的思路就是：任意取一条链表，遍历每个节点的 next 是否等于用另一个链表每一个节点的 next。假设长短链表的长度分别是 `m` 和 `n`。这种做法的时间复杂度是 O(m\*n)。因为本质上是走了 `m * n` 次循环。这种方法在数据量很大的情况下会 Time Limit Exceeded。

如果我们用两个指针分别走两个链表，那么长链表的指针会比短链表的指针**慢**到达结尾处 `m - n `个单位，而且这些慢的步子全来自于未交汇前链表长度的差。那么如果我们让短链表指针下一次走长链表，长链表的指针下一次走短链表，那么当它们第一次相遇时，正好是到了交汇处（*如果两个链表不交汇，它们会一起到达链表末尾 None*）。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        a, b = headA, headB
        while a is not b: a, b = a.next if a else headB, b.next if b else headA
        return a
```