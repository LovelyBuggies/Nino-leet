# [21. Valid Parenthesis](https://leetcode.com/problems/merge-two-sorted-lists/)

## 问题

合并两个已排序的链表，并以新链表的形式返回。新列表是升序的，通过将两个列表的节点拼接在一起来创建。

**例子：**

```markdown
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

## 思路

首先，我们先来尝试一种可读性较好的实现方法：创建一个新的链表，按照值的大小决定节点的指向。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(0)
        n, n1, n2 = head, l1, l2
        while n1 and n2:
            if n1.val < n2.val:
                n.next = n1
                n1 = n1.next
            else:
                n.next = n2
                n2 = n2.next
            n = n.next
        n.next = n1 or n2   
        
        return head.next
```

但是，我们其实可以有更简单的做法：如果两条链都是非空的，我们首先需要确保`l1`是较小值的节点，用它的头作为结果，然后去合并其后面的链表；否则，直接返回就好了。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
```

