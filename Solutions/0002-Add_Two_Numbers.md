# [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## 问题

你有两个**非空**链表代表两个非负整数。这些数字以**相反**的顺序存储，每个节点包含一个数字。将这两个数字相加并以链表的形式返回。

您可以假设这两个数字不包含任何前导零，除了数字0本身。

**例子：**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## 思路

依次遍历链表的每一个节点，如果有进位就计为carry。判断是否继续生成新链表的是判断是否list1、list2是否还存在`next`，以及是否存在进位。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def addTwoNumbers(self, l1, l2):
        
        carry = 0
        root = node = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            node.next = node = ListNode(val)
            
        return root.next
```

