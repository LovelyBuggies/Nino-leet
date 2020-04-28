# [501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

## 问题

给定一个有重复元素的二叉搜索树，找到这棵二叉搜索树中元素的众数。

本题的二叉搜索树定义为：

- 节点的左子树只包含值小于或等于节点的键值的节点。
- 节点的右子树只包含值大于或等于节点的键的节点。
- 左子树和右子树也必须是二叉搜索树。

**例子：**

```
Input: [1,null,2,2]

   1
    \
     2
    /
   2

Output: [2]
```

**注意：**假如给定的二叉搜索棵树中含有多个众数，将它们存入一个数组返回。

**跟进：**你能在不使用额外内存的情况下解决这个问题么（*假设由递归引起的隐式堆栈空间不计算在内*）？

## 思路

这个题目我们采取的思路是：

- 遍历该树，用一个字典存储，键是每个元素，值是出现次数。
- 计算最多出现的次数，并返回出现该次数对应的键。

## 答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def findMode(self, root: TreeNode) -> List[int]:
        
        def helper(root, res):
        
            if not root: return res
            if str(root.val) in res: res[str(root.val)] += 1
            else: res[str(root.val)] = 1
            helper(root.left, res)
            helper(root.right, res)
            return res
        
        # 遍历并存储元素出现次数
        res, count, modes = helper(root, {}), 0, []
        
        # 计算众数
        for key, value in res.items():
            if value > count: modes, count = [key], value
            elif value == count: modes += [key]
            
        return modes
```