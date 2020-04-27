# [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## 问题

假设一个按升序排序的数组在某个未知的主元处旋转，比如 `[0,1,2,4,5,6,7]` 可能会变成 `[4,5,6,7,0,1,2]`。

在一个数组中，找到一个目标值：如果找到，返回 `true`；否则，返回 `false`。

**例子：**

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**跟进：**

- 这是第 33 题的跟进题目，这个题目中的数组可能包含重复元素。
- 这个会影响时间复杂度么？怎样影响？为什么会影响？

## 思路

当用 Python 一切变得很简单。我们可以尝试用 Python 内置的函数 `index()`（ `index()` 和 `find()` 有区别的，`find()` 找不到会返回 -1，但它不能用于list）。只需要两行代码就可以轻松搞定：

```python
if target not in nums:  return -1
else:   return nums.index(target)
```

同第 33 题一样，我们可以用一种类似于二分查找的方法，分别确定最大最小元素的 index 就可以当成一个真正的有序数列来处理了。

## 答案

```python
class Solution:
    
    def search(self, nums: List[int], target: int) -> bool:
        
        if not len(nums): return False
        
        # 查找最大最小元素
        high, l = 0, len(nums)
        while high < l - 1:
            if nums[high+1] < nums[high]: break
            else: high += 1
        
        # 二分查找
        low = high - l + 1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]: high = mid - 1
            elif target > nums[mid]: low = mid + 1
            else: return True

        return False       
```
