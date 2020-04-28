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



## 答案

```python
import itertools

class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res, nums = [], sorted(nums)
        for k in range(len(nums) + 1): res += itertools.combinations(nums, k)
            
        return list(set(res))
```