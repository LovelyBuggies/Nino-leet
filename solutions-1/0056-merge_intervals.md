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
- 为了避免索引错位，`intervals[idx]` "蜡炬成灰泪始干"，变成了 `[]`；而 `intervals[idx+1]` "病树前头万木春"，变成了新的大区间。
- 最后，我们"剥茧抽丝"，把非空区间取出来返回就好了。

## 答案

```python
class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        for idx in range(len(intervals) - 1):
            if intervals[idx][1] >= intervals[idx+1][0]: intervals[idx], intervals[idx+1] = [], [intervals[idx][0], max(intervals[idx+1][1], intervals[idx][1])]
        while [] in intervals: intervals.remove([])
            
        return intervals
```