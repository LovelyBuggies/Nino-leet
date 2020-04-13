# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## 问题

给定一个升序的整数数组 `nums`，找出其中第一个和最后一个的目标数位置。要求的算法的时间复杂度应该为 O(log n)。

如果目标数根本不在数组中，请返回 `[-1, -1]`。

**例子：**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## 思路

要求的时间复杂度为 O(n) ??? 那直接用两个迭代变量从头到尾和从尾到头迭代一遍不就好了？这个题目是可以达到 O(log n) 的。如果你对 Python 轮子比较熟悉，你可能会想到 `bisect`，然后你就可以直接解决了。

```python
l, r = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
return [l, r] if l <= r else [-1,-1]
```

让我们看看是怎么实现这个轮子的：



## 答案

```python
import numpy as np

class Solution:
    
    def search(self, nums, target):
        
        if not len(nums):   return -1
        
        high = np.argmax(nums)
        low = high - len(nums) + 1
        
        while low <= high:
            mid = (low+high) // 2
            if target < nums[mid]:   high = mid - 1
            elif target > nums[mid]: low = mid + 1
            else: return mid + len(nums) if mid < 0 else mid

        return -1
```

