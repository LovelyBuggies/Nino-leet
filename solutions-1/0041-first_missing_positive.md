# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

## 问题

给定一个无序的整数数组，找到其中缺少的最小正整数。

**例子：**

```
Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1
```

## 思路

当用 Python，一切变得很简单。


## 答案

```python
class Solution:
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        target = 1
        while target in nums:
            target += 1
            
        return target
```

