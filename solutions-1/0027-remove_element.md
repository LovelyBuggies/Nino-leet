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

当然一个很直观的做法就是用集合工具。但是需要注意，集合是无序的，所以原本的顺序被打乱了，我们还得重新排序，这耽误了不少运行时间。

```python
class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        nums[:] = sorted(list(set(nums)))
        
        return len(nums)
```

于是，我们可以用这个思想。首先，用两个指针计算一个数字出现了几次，当然这个题目需要"保证"出现最多一次，所以可以用一个索引就好了，因为快慢指针间隔恒为 1。然后，对于第二个重复元素，直接 remove。需要小心的是，这时候数组长度变短了，如果还按照以前的长度进行遍历，索引会越界，所以干脆维护一个数组即时长度变量并用 while 决定循环好了。

## 答案

```python
class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx, l = 0, len(nums)
        while idx < l - 1:
            if nums[idx+1] == nums[idx]: 
                nums.remove(nums[idx+1])
                l -= 1
            else: idx += 1  
        
        return len(nums)
```

*然鹅，这个方法运行速度还不如 set 法呢 :<*