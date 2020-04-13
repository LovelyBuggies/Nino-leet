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

实现这个轮子其实还是挺烧脑的。精髓在于即使第一次找到了 `target`，也不扔到 `res` 里，而是保持耐心，直到找到最左/右的 `target` 的位置。


## 答案

[The implementation of `bisect_*`.](https://github.com/python/cpython/blob/3.8/Lib/bisect.py)

```python
class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        
        # bisect left
        low, high = 0, len(nums)
        while low < high:
            
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else: high = mid
        res.append(low)
        
        # bisect right - 1
        low, high = 0, len(nums)
        while low < high:
            
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid
            else: low = mid + 1
        res.append(low - 1)
        
        return res if res[0] <= res[1] else [-1, -1]
```

