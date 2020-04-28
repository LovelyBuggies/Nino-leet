# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## 问题

给定一个数组 `nums`，将其中所有的值为 0 的元素移到末尾，并保持原来非 0 元素的顺序。

**例子：**

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**注意：**

1. 你必须  [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) 地实现这个问题。
2. 最小化操作步骤。

## 思路

考虑到这个题目最后添加的 0 都是无差别的，一个直观的解法就是遍历一遍。遇到 0 就 remove，并计算一共多少个 0，然后添加到数组的后面。

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = 0
        while 0 in nums:
            count += 1
            nums.remove(0)
            
        nums[:] = nums + [0] * count
```

当然还是那个老生常谈的 `in` 产生额外时间成本的问题，为了克服这点，我们可以动态维护数组的实时长度。

## 答案

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        idx, l, c = 0, len(nums), 0
        while idx < l:
            if nums[idx] == 0:
                nums.remove(nums[idx])
                l, c = l - 1, c + 1
            else: idx += 1
                
        nums[:] = nums + [0] * c
```