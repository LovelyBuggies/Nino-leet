# [27. Remove Element](https://leetcode.com/problems/remove-element/)

## 问题

给定一个数组 `nums` 和一个值 `val` ， [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) 地移除其中所有值为 `val` 的项目。

不要额外分配空间，要求  [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) 地移除，并使用 O(n) 大小的空间。

你可以改变原先数组中元素的顺序。

**例子：**

```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.


Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
```

**澄清：**

你也许会困惑为什么返回的是一个数组（按理说应该是个整数）？因为 LeetCode 把这个数组的引用传了进来。

## 思路

一种很简单的办法就是判断元素是否还在数组中，如果在的话就移除。

```python
class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        
        while val in nums: nums.remove(val)
            
        return len(nums)
```

但是这样我们要每次循环都 `in` 一下，其实时间复杂度是 O(n^2) 的。所以我们用一个变量 `l` 动态记录数列长度。

## 答案

```python
class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        
        idx, l = 0, len(nums)
        while idx < l:
            if nums[idx] == val: 
                nums.remove(val)
                l -= 1
            else: idx += 1
        
        return len(nums)
```
