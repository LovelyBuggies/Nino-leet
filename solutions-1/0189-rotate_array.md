# [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

## 问题

给定一个数组，右移数组 `k` 步，其中 `k` 是一个非负整数（*但有可能大于数组长度*）。

**跟进：**

- 尽可能考虑多种解。
- 你能 in-place 地实现这个题目么？

**例子：**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## 思路

这个题目我们采取切片的方法，尽管广义上这并不是 in-place 的方法，但它确实快啊！

## 答案

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
```