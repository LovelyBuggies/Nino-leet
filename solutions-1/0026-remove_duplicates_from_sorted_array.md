# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## 问题

给定一个**顺序的**可能含有重复元素的整数数组 `nums`，[in-place](https://en.wikipedia.org/wiki/In-place_algorithm) 地删除掉其中重复的元素，使其中的元素最多出现一次。

不要额外分配内存给其他的数组，用空间复杂度为 O(1) 的方法去**修改** `nums`。

**例子：**

```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.


Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

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