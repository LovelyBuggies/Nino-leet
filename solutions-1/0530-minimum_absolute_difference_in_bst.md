# [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## 问题

给定一个非负值的二叉搜索树，求任意两个节点值之间的[最小绝对差](https://en.wikipedia.org/wiki/Absolute_difference)。

**例子：**

```
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
```

**注意：**

- 二叉搜索树中至少有两个节点。
- 这个题和第 783 题一样。

## 思路

我们利用二叉搜索树中序遍历结果升序的性质，得到中序遍历结果。并维护一个计算最大绝对差的变量，计算两两之间的差就好了。

## 答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        vals = []
        def helper(root, vals):
        
            if not root: return
            helper(root.left, vals)
            vals.append(root.val)
            helper(root.right, vals)
            return vals
        
        
        vals = helper(root, vals)
        res = max(vals)
        for idx in range(1, len(vals)):
            res = min(res, vals[idx] - vals[idx-1])
            
        return res
```