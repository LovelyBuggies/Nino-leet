# [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## 问题

给定一个二叉树，返回后序遍历的结果。*这个题目是第 94 题和第 144 题的姐妹问题。*

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
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        return [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right) if root else []
```

### 迭代法

迭代法的基本思路就是：如果当前节点存在，就存储它的 value 添加到返回值中，并将其存在栈中，然后左寻用其左节点替代当前节点；如果当前节点不存在，则用栈顶节点替代当前的节点，并用其右节点迭代这个节点。

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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        def helper(root, res):
        
            if not root: return res
            res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)
            return res
        
        res = helper(root, [])
        
        return res
    
    
    # 迭代法
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, res = [], []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
            
        return res
```