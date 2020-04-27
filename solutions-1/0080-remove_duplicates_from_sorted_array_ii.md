# [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## 问题

给定一个**顺序的**可能含有重复元素的整数数组 `nums`，[in-place](https://en.wikipedia.org/wiki/In-place_algorithm) 地删除掉其中重复的元素，使其中的元素最多出现两次。

不要额外分配内存给其他的数组，用空间复杂度为 O(1) 的方法去**修改** `nums`。

**例子：**

```
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.


Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
```

**澄清：**

你也许会困惑为什么返回的是一个数组（按理说应该是个整数）？因为 LeetCode 把这个数组的引用传了进来。

## 思路

这个题目一个很直观的做法就是安排一个常数数据结构，比如字典，来记忆每个元素出现的次数，一但超过了 2 次就用一个 None（或者其他）标记标识一下，然后 second-pass 将这些 None 元素剔除。

```python
class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        d = {}
        for idx in range(len(nums)):
            if not str(nums[idx]) in d: d[str(nums[idx])] = 1
            elif d[str(nums[idx])] == 2: nums[idx] = None
            else: d[str(nums[idx])] += 1
        
        while None in nums: nums.remove(None)
        return len(nums)
```

然而，让我们思考一下这几个问题：

-  顺序数组这个条件怎么用？
- 能不能不用额外的字典来计算一个元素出现了几次？
- 能不能不要遍历两边？

于是，诞生了如下的思想。首先，用两个指针计算一个数字出现了几次，当然这个题目需要"保证"出现最多两次，所以可以用一个索引就好了，因为快慢指针间隔恒为 2。然后，对于第三个重复元素，直接 remove。需要小心的是，这时候数组长度变短了，如果还按照以前的长度进行遍历，索引会越界，所以干脆维护一个数组即时长度变量并用 while 决定循环好了。

## 答案

```python
class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx, l = 0, len(nums)
        while idx < l - 2:
            if nums[idx+2] == nums[idx]: 
                nums.remove(nums[idx+2])
                l -= 1
            else: idx += 1  
        
        return len(nums)
```