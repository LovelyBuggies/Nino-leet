# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## 问题

将给定链表反转。

**例子：**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

## 思路

### 递归法

### 迭代法

迭代法的基本思路是反转每个 next 指向关系。Talk is cheap, let's see code！

在头节点存在的情况下，每次循环 `while head`：

- 用头节点作为现在节点 `curr = head`。
- 将头节点设置为下一个节点 `head = head.next`。
- 将现在节点的 next 指到之前保留的 prev 节点 `curr.next = prev`。
- 更新 prev 节点为现在的节点 `prev = curr`。

注意遍历完之后头节点是空的，要返回 curr 或者 prev 节点哦。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # 迭代法
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
```