# [61. Rotate List](https://leetcode.com/problems/rotate-list/)

## 问题

给定一个链表，将其右移 k 位，k 非负。

**例子：**

```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

## 思路

首先我们先介绍一下当 `k not >> len(L)` 的情况下的较好方法——循环法；以及讨论一下 `k >> len(L)` 的较好方法（适合于本题的测试样例）。

无论哪种方法，我们都是基于这样的思路：

1. 找到新的头节点。
2. 切断头节点与其前面节点的联系。
3. 为链表末节点和旧的头节点添加联系。

然后我们分别用循环法和取模法实践这个思路。最后我们比较一下两者性能上的差距。

### 循环法

循环法基于以下假设：

- 对于空链表 `L = []`或者不需要右移 `k = 0` 的链表，直接返回就可以。
- 如果 `k` 超过了 `L` 的长度，则折返回来找新的头节点。
- 如果右移正好使头新的节点回到原处，那么当作不需要右移处理。

这样我们就能写出如下代码：

```python
class Solution:
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k: return head
        
        slow = fast = head
        while k > 0:
            fast = fast.next if fast.next else head
            k -= 1
			
        if fast == head: return head
		
		# slow is the previous node of the new head
        while fast.next: slow, fast = slow.next, fast.next
        
		# cut the circular link
        tmp = head
		head = slow.next if slow.next else head
		slow.next = None
		
		# establish the new link
        node = head
        while node.next: node = node.next
        node.next = tmp
        
        return head
```

看起来不错？Opps... 有测试样例超时了，`L = [1, 2, 3], k = 2000000000`。看来我们还是用另一种方法吧。

### 取模法

取模法和循环法在思路上都是一样的，只不过实现手段有些差异。差异主要体现在第一步找新的头节点上，因为大值 `k` 在这一步拉开了差距。

取模法基于的以下假设：

- 用 `k` 除以 `len(L)` 的模作为真正的右移距离（排除掉无用的循环右移）。
- 对于空链表 `L = []`或者不需要右移 `k = 0` 的链表，直接返回就可以。
- `k` 不可能超过 `L` 的长度，所以右移不可能使头新的节点回到原处。

这样我们就能写出答案里的代码了。

### 性能比较

读到这里，你肯定会好奇或者思考为什么看起来多了一次遍历找 `len(L)` 的取模法反而可以 defeat 循环法呢？虽然取模法多了一次遍历，`k` 次循环，但人家每次的循环可是工作量都小啊。更直观点，当 `k` 很大的时候，主要的计算量就在 `k` 次循环里，让我们看看每次循环两个方法分别干了什么。

```diff
- fast = fast.next if fast.next else head
+ node = node.next
k -= 1
```

原来 `k` 次循环里，每次循环法都要进行一次条件判断来赋值，难怪它慢。如果已知 `k not >> len(L)`，那么采取循环法不用一次遍历找长度还是比较 reasonable 的。

## 答案

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head: return head
        
        count, node = 0, head
        while node:
            count += 1
            node = node.next
        
        k %= count
        
        if not k: return head
        
        slow = fast = head
        while k > 0:
            fast = fast.next
            k -= 1
        
        while fast.next:
            if not slow.next: return head
            slow, fast = slow.next, fast.next
        
        slow.next, head, tmp = None, slow.next if slow.next else head, head 
        node = head
        while node.next: node = node.next
        node.next = tmp
        
        return head
```