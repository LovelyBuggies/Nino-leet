# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## 问题

给定一个区间集合，合并所有重叠区间。

**例子：**

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## 思路

这个题目的常规做法其实还是挺直观的：

- 首先，先对列表进行排序，这样区间就会按照起点的大小按序排列。
- 对于每一个区间，区间的终点有三种情况。
  - 小于下一个区间的起点：直接不用合并。
  - 大于下一个区间的起点，小于下一个区间的终点：取下一个区间的终点。
  - 大于下一个区间的终点：取这个区间的终点。

## 答案

```python
class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        
        reach = 0
        for idx, num in enumerate(nums[:-1]):
            # the farthest reach
            reach = max(reach, idx + num)
            # if walk outreach the reach scope, return false
            if not idx < reach: return False
            
        return True
```