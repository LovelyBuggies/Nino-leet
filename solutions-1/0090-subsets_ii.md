# [90. Subsets II](https://leetcode.com/problems/subsets-ii/)

## 问题

给定包含重复整数的数组 `nums`，返回它所有的子集。

**注意：**子集中不能含有重复的集合。

**例子：**

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

## 思路

其实我们完全可以用和第 78 题一样的思路，最后去重一下就可以了。但是，这个题目略坑的一点就是输入不一定是顺序的，比如 `[4,4,4,1,4]`，但题目答案却认为毕竟子集也是一个 set 嘛，所以 `[4,4,4,1]` 和 `[4,4,1,4]` 是一样的。为了避免中间的 1 造成前后 4 在组合中意义不同，可以直接先对输入数组进行排序，这样 4 就不会在 1 之前了。

## 答案

```python
import itertools

class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res, nums = [], sorted(nums)
        for k in range(len(nums) + 1): res += itertools.combinations(nums, k)
            
        return list(set(res))
```