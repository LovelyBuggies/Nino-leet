# [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## 问题

给定一个二叉树，返回中序遍历的结果。*这个题目是[第 144 题](./0144-binary_tree_preorder_travesal.md)和[第 145 题](./0145-binary_tree_postorder_travesal.md)的姐妹问题。*

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

### 递归法

递归法确实挺简单的，在这里就不多赘述了。答案里给的是一种一般的递归方法，这里给出一种简洁的解决方法。

```python
class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
```

### 迭代法

迭代法的基本思路就是：如果当前节点存在，就将其存在栈中，并左寻用其左节点替代当前节点；如果当前节点不存在，则用栈顶节点替代当前的节点，并存储它的 value 添加到返回值中，添加完之后，用其右节点迭代这个节点。

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
    
    
    # 迭代法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, res = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
```