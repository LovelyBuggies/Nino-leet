# [57. Insert Interval](https://leetcode.com/problems/insert-interval/)

## 问题

给定一个区间集合包含 n 个非重叠区间，插入一个新区间（如果有必要，请合并）。

你可以假设这些区间最初是根据它们的开始时间排序的。

**例子：**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## 思路

这个题目一个很 intuitive 的方法就是用第 56 题第框架，虽然耗时多了点，但是 scalability 较好，这种方法甚至可以用来 insert interval**s**.

## 答案

```python
class Solution:
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals)
        for idx in range(len(intervals) - 1):
            if intervals[idx][1] >= intervals[idx+1][0]: intervals[idx], intervals[idx+1] = [], [intervals[idx][0], max(intervals[idx+1][1], intervals[idx][1])]
        while [] in intervals: intervals.remove([])
        return intervals
```