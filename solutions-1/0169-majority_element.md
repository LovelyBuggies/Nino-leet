# [169. Majority Element](https://leetcode.com/problems/majority-element/)

## 问题

给定一个 `n` 个元素的数组，找到其中的主要元素。主要元素是指出现超过过 `[n/2]` 次的元素。

你可以假定数组非空，并且有一个主要元素存在。

**例子：**

```
Input: [3,2,3]
Output: 3

Input: [2,2,1,1,1,2,2]
Output: 2
```

## 思路

设置一个字典存储元素出现的次数，剩下的就无需赘言了。

## 答案

```python
class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        
        d, l = {}, 0
        for num in nums:
            l += 1
            if str(num) in d: d[str(num)] += 1
            else: d[str(num)] = 1
        
        for idx, val in d.items():
            if val > l / 2: return idx
```