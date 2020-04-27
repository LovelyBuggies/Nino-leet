# [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## 问题

给定包含独特整数的数组 `nums`，返回它所有的子集。

**注意：**子集中不能含有重复的集合。

**例子：**

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## 思路

这个题目是第 77 题的变种，就是计算所有不同 k 组合的集合。

## 答案

```python
import itertools

class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        for k in range(len(nums) + 1):
            res += itertools.combinations(nums, k)
            
        return res
```