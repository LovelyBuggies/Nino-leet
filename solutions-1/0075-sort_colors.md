# [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

## 问题

给定一个 n 个元素颜色为红、白、蓝的数组，按红、白、蓝的顺序对它进行 [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) 的排序，让其中相同颜色的元素相邻。

这里我们分别用 0、1、2 表示 红、白、蓝的元素。

**例子：**

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

## 思路

我们可以通过直接 sort 来解决。


## 答案

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
```