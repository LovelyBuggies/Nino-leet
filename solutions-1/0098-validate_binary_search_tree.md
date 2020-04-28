# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## 问题

给定一个二叉树，判断它是否是一个二叉搜索树。

这里的二叉搜索树定义如下：

- 一个节点的左子树只含有值小于该节点值的节点。
- 一个节点的右子树只含有值大于该节点值的节点。
- 左右子树都必须也为二叉搜索树。

**例子：**

```
    2
   / \
  1   3

Input: [2,1,3]
Output: true

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## 思路

这个题目可以根据二叉搜索树的定义来操作，但是难点在于判断左子树中节点的最大值小于根节点、判断右子树中节点的最小值大于根节点。

一个好用的方法是利用中序遍历。二叉搜索树有个好用性质：**中序遍历一棵二叉搜索树的结果是升序的**。有了这个性质，这个题目就容易多了。另外还要判断有没有值相同的节点就好了。

## 答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        res = []
        
        def helper(root, res):
        
            if not root: return res
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
            return res
        
        
        # 中序遍历结果
        res = helper(root, res)
        
        # 判断升序和重复
        for idx in range(1, len(res)):
            if not res[idx] > res[idx-1]: return False

        return True
```