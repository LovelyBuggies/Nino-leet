# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## 问题

将给定链表反转。

**例子：**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

## 思路

迭代法和递归法的基本思路都是反转每个 next 指向关系，实现起来也比较类似。Talk is cheap, let's see code！

### 递归法

首先定一个递归函数。输入参数包含其之前的节点 `prev` 和当前节点 `curr`，每次递归中：

- 首先记录下一个节点 `tmp = curr.next`。
- 然后改变指向关系 `curr.next = prev`。
- 将保存节点  `curr` 和 `tmp` 分别作为下层递归的 `prev` 和 `curr `传入。

### 迭代法

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
    
    # 递归法
    def reverseList(self, head: ListNode) -> ListNode:
        
        def helper(prev, curr):
            
            if not curr: return prev
            tmp = curr.next
            curr.next = prev
            
            return helper(curr, tmp)
          
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