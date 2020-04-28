# [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## 问题

给定一个二叉树，返回中序遍历的结果。

**例子：**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

**跟进：**递归解很简单，你能迭代地做吗?

## 思路

递归确实挺简单的，就不再赘述了。

## 答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 递归法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def helper(root, res):
        
            if not root: return res
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
            return res
        
        res = helper(root, [])
        
        return res
```