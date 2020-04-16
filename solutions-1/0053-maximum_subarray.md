# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## 问题

给定一个整数数组 `nums`，找到最大和的连续子数组（至少包含一个元素）并返回它的和。

**例子：**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**下一步：**

如果你已经找到了 O(n) 的解决方案，那么尝试使用分治法编写另一个解决方案，这种方法更加微妙。

## 思路

这个题目我们暂且用一个比较简单的动态规划来解决。核心思想就是最大子数列的头一定是个正数（因为负数的头对最大子数列和没有积极影响）：如果前面的累加结果为负数，那么我们就可以不要了。值得注意的是，这是动态规划最经典的题目之一，是 Jon Bentley 在1984年 ACM 交流会提出的。

## 答案

```python
class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        for idx in range(len(nums) - 1):
            if nums[idx] > 0:  nums[idx + 1] += nums[idx]
        return max(nums)
```