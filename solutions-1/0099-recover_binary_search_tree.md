# [99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

## 问题

二叉搜索树的两个节点因为误操作交换了位置。在不改变其结构的情况下，复原这棵二叉搜索树。

**例子：**

```
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2


Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

**跟进：**

- O(n) 空间的解答方案是十分直观的。
- 你能设计一个常数空间的解决方案么？

## 思路

这个题目我们使用二叉搜索树中序遍历升序的性质，用中序遍历找到错位的两个节点，然后更改这个两个节点的值就好了。我们 generalize 一下，假如不只两个点错位了，该怎么办呢？我们可以对二叉搜索树按照正确的顺序重新赋值就好了。

## 答案

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # 中序遍历找误点
        def helper(root, res):
        
            if not root: return res
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
            return res
        
        
        # 按正确顺序重新赋值
        def helper2(root, res):
            
            if not root: return res
            res = helper2(root.left, res)
            root.val = res[0]
            res.remove(root.val)
            res = helper2(root.right, res)
                
            return res
        
        
        helper2(root, sorted(helper(root, [])))
```