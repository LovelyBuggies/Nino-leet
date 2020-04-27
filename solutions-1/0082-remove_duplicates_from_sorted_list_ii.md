# [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## 问题

给定一个链表，删除其中所有**重复过**的元素，保证只有**曾经**独一无二的元素留在原链表中。

返回结果依然保持有序状态。

**例子：**

```
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Input: 1->1->1->2->3
Output: 2->3
```

## 思路

因为链表本身是有序的了，我们的主要思路是比较两个相邻节点是否 value 相同，如果相同的话就将其 remove 掉。那么具体该如何 remove 呢？

1. 第一个方法就是维护一个动态变量：发现重复之后，记录下来这个重复元素的值，方便后面的对比；如果没有重复则更新为 None。
2. 第二个方法是只删除其中前一个节点，然后拿后面的节点与之后的链表接着比较。
3. 第三个方法就是用两个指针，记录下来重复元素的开始和末尾点，然后一下子 remove 掉这其中的所有节点。

我们这里用的是第二种方法。但是有两个地方的重复需要我们特别注意，头重复和尾重复。我们分别采用如下的操作方法；

- **头重复：**设置一个 dummy node 作为虚头节点。这样头节点就被对待成像普通节点一样。
- **尾重复：**因为当我们发现一处重复之后，我们并没有把它们都清除，我们留了后一个来进行后续比较，所以最后一个节点即使重复也被保留。但我们可以维护一个变量来记录每个节点是否是被暂时保留的、然而应该被移除的节点，并在最后判读一下。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        
        # 设置 dummy 节点，处理头重复
        head, head.next = ListNode(None), head
        
        # 维护一个移除记录变量，遍历整个链表
        bool_remove, node = False, head
        while node.next.next:
            if node.next.val == node.next.next.val:
                node.next = node.next.next
                bool_remove = True
            elif bool_remove:
                node.next = node.next.next
                bool_remove = False
            else: node = node.next
              
        # 处理尾重复
        if bool_remove: node.next = None
        
        return head.next
```
