# [1 Two Sum](https://leetcode.com/problems/two-sum/)

## 问题

给定一个整数数组，返回两个数字的**索引**，使它们加起来等于一个特定的目标。

您可以假设每个输入将**恰好**一个解决方案，并且您不能两次使用*相同的*元素。

**例子：**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## 思路

 因为只需要两个数相加，遍历list，找到元素的对应值的index就好了。注意，在测试集 input: [3,2,4]，target=6的情况下，我们找对应值的list应该为`num[index+1:]`，这样既可以避免找到同一个值，也可以减少相应的搜索成本。

## 答案

```python
class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) < 2:
            return False
        
        for idx, num in enumerate(nums):
            if target - num in nums[idx+1:]:
                return [idx, idx+1+nums[idx+1:].index(target - num)]
```

