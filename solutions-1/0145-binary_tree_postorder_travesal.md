# [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## 问题

给定一个二叉树，返回后序遍历的结果。*这个题目是[第 94 题](./0094-binary_tree_inorder_travesal.md)和[第 144 题](./0144-binary_tree_preorder_travesal.md)的姐妹问题。*

**例子：**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```

**跟进：**递归解很简单，你能迭代地做吗?

## 思路

### 递归法

递归法确实挺简单的，在这里就不多赘述了。答案里给的是一种一般的递归方法，这里给出一种简洁的解决方法。

```python
class Solution:
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
```

### 迭代法

这个题目和其姐妹问题的区别在于，纯迭代有点麻烦。但是后序遍历有个重要的性质，就是：如果我们在先序中先遍历右子树，那么将会得到后序遍历的反数组。我们利用这个性质，就变得和第 144 题很相似。

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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        def helper(root, res):
        
            if not root: return res
            helper(root.left, res)
            helper(root.right, res)
            res.append(root.val)
            return res
        
        res = helper(root, [])
        
        return res
    
    
    # 迭代法
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, res = [], []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
            
        return res[::-1]
```