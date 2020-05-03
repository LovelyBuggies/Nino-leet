# [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

## 问题

给定两棵二叉树，检验它是否是自己的镜像。

**例子：**

```
Input:
    1
   / \
  2   2
 / \ / \
3  4 4  3

Output: true


Input:
    1
   / \
  2   2
   \   \
   3    3

Output: false
```

## 思路

这个题目可以用递归法和循环法解决，在此给出递归解决方案。递归的主要思路是，判断两棵树是否是镜像的。

- 首先判断两个节点是不是都为空，如果是则算对称。
- 如果两个节点都不为空且值相等，那么可以进行下一步判断，否则直接返回不对称。
- 判断这两个值相等的节点的四棵子树是否也互为镜像。

## 答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def helper(left, right):
            
            if not left and not right: return True
            if left and right and left.val == right.val: return helper(left.left, right.right) and helper(left.right, right.left)
            
            return False
        
        
        return helper(root, root)
```