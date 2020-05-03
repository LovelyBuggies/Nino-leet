# [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

## 问题

给定一个链表，返回循环开始的节点。如果没有循环，则返回 None。

为了在给定的链表中表示一个循环，我们使用一个整数 `pos` 来表示链表尾连接到的链表中的位置。如果 `pos` 是 -1，那么链表中就没有循环。

**注意：**不要修改链表。

**例子：**

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)



```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)



```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list
```

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)



**跟进：**

你可以用常数内存实现么？

## 思路

![](https://assets.leetcode.com/users/lovelybuggies/image_1588299577.png)

这个问题中，我们使用三个指针，`slow` 和`fast` 用来**找到链表快慢指针在环中相遇的地方**；`slow` 和`node` 用来**找到链表中环开始的地方**。

**符号标注：**

- `l`：链表头到环开始地方的距离。
- `d`：链表环开始的地方到快慢指针相遇点的距离。
- `c`：链表中环的长度。
- `k`：链表快慢指针相遇点到环开始地方的距离。

**迭代规则：**

1. `fast` 快指针每次走 2 步，`slow` 慢指针每次走一步。
2. 在快慢指针相遇之后，`node` 指针和 `slow` 慢指针每次走 1 步。

**重要事实：**

1. **在慢指针进入环中之后**，快指针会"套"慢指针一圈（比慢指针多走一圈）。
2. `k = l` （红色虚线是相等的）。并且在快慢指针相遇之后，`node` 指针和 `slow` 慢指针会在环起始点相遇。

**解释说明：**

1. 当慢指针进入环之后，它们在同样的环中迭代。因为快指针的速度是慢指针的两倍，快指针会套慢指针一圈。
2. 相遇时，慢指针走过的距离是 `S1 = l + d`，而快指针是 `S2 = l + c + d`。考虑到同样时间（次数）内，快指针是慢指针速度的 2 倍，那么 `S2 = 2 * S1`。因此，`k = l` （红色虚线是相等的）。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return None
        
        a = b = head
        while b and b.next:
            a, b = a.next, b.next.next
            if a == b: break
        
        b = head
        while b and a:
            if b == a: return b
            a, b = a.next, b.next
            
        return None
```