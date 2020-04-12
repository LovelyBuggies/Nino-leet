# 2. Add Two Numbers

## 问题

你有两个**非空**链表代表两个非负整数。这些数字以**相反**的顺序存储，每个节点包含一个数字。将这两个数字相加并以链表的形式返回。

您可以假设这两个数字不包含任何前导零，除了数字0本身。

**例子：**

```text
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## 思路

传统做法是：依次遍历链表的每一个节点，如果有进位就计为carry。判断是否继续生成新链表的是判断是否list1、list2是否还存在`next`，以及是否存在进位。Discussion有个大神将这个链表转化成了int来进行加减，然后赋值给了新的链表，代码极其简短。这个方法会出现问题。因为当链表特别长、代表整数特别大的情况下，Python3不容易对这种大数进行四则运算。所以这里我还是用的传统做法。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

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

