# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## 问题

假设一个按升序排序的数组在某个未知的主元处旋转，比如 `[0,1,2,4,5,6,7]` 可能会变成 `[4,5,6,7,0,1,2]`。

在一个数组中，找到一个目标值：如果找到，返回它的 index；没有的话返回 -1。数组中没有重复元素，要求算法时间复杂度 O(log n)。

**例子：**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## 思路

当用 Python 一切变得很简单。我们可以尝试用 Python 内置的函数 `index()`（ `index()` 和 `find()` 有区别的，`find()` 找不到会返回 -1，但它不能用于list）。只需要两行代码就可以轻松搞定：

```python
if target not in nums:  return -1
else:   return nums.index(target)
```

尽管这个方法十分简单，但它的时间复杂度是 O(n) （[Python Built-in Complexity](https://wiki.python.org/moin/TimeComplexity)），但要求的算法时间复杂度是 O(log n)。当然，在后面的练习 34 中，你可以看到也可以用 bisect 轮子实现，但是这里我们主要探讨的还是环式二分查找的方法。

考虑到这点，我们可以用一种类似于二分查找的方法，分别确定最大最小元素的 index 就可以当成一个真正的有序数列来处理了。*题外话：其实新方法的运行时间并不比 `index()` 方法小，但是毕竟时间复杂度不是真正意义上的运行时间。* :)

## 答案

```python
class Solution:
    
    def search(self, nums, target):
        
        if not len(nums):   return -1
        
        idx, l = 0, len(nums)
        
        while idx < l - 1:
            if nums[idx+1] < nums[idx]: break 
            else: idx += 1
        
        high = idx
        low = high - l + 1
        
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:   high = mid - 1
            elif target > nums[mid]: low = mid + 1
            else: return mid + l if mid < 0 else mid

        return -1
```

