# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## 问题

给定一个链表，从链表的末尾删除第n个节点并返回它的头。

**例子：**

```markdown
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

## 思路

这个题目一个很intuitive的做法就是遍历一边链表，得到链表长度`num`，然后找到第`num-n`个链表节点即可。注意事项就是，如果是倒数第`num`个元素，操作可能会特殊一点。我们把这种操作normalized一点，就是加一个起始节点`start`作为头节点，然后最后返回的起始的`next`就好了。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        start = ListNode(0)
        start.next = head
        head = start
        
        node, num = head, 0
        while node:
            node = node.next
            num += 1
        
        node, idx = head, 0
        while idx < num - n - 1:
            node = node.next
            idx += 1
            
        node.next = node.next.next
        return head.next
```

但是Leetcode想让我们用一种"one-pass"的方法完成这个题目。我们可以采用一个双线遍历的做法，一个遍历迭代器是`fast`，比另一个迭代器`slow`跑快n个节点，这样当`fast`抵达终点之后，`slow`恰好到了第`num-n`个节点（因为它`fast`慢n个节点），也就是到了第倒数第n个节点。这样我们就能在一个循环中删除倒数第`n`个节点了。有趣的是，其实这种方法从运行时间来看反而更长，但是节省了一些内存。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
```

