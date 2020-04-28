# [100. Same Tree](https://leetcode.com/problems/same-tree/)

## 问题

给定两棵二叉树，检验它们是否相同。

如果两个二叉树在结构上相同，且节点具有相同的值，则认为它们是相同的。

**例子：**

```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true


Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false


Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

## 思路

这个题目思路还是蛮简单的，首先判断结构相同，然后判断值相同，最后递归到子树。

## 答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p or not q: return p == q
        elif p.val != q.val: return False
        else: return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```