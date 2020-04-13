# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

## 问题

给定一个升序的整数数组 `nums`。如果`target` 在 `nums` 中，找出目标 `target` 的 index；如果不在，找到应该插入它的 index。数组不重复。

**例子：**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## 思路

这个题目也是二分查找的一个应用，如果你对 `bisect_*` 比较熟悉的话，你会发现所求的 index 实际上就是 `bisect_left`。这种情况下，算法的时间复杂度为 O(log n)。


## 答案

[The implementation of `bisect_*`.](https://github.com/python/cpython/blob/3.8/Lib/bisect.py)

```python
class Solution:
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums)
        while low < high:

            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else: high = mid
                
        return low
```

