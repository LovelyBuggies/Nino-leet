# [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/)

## 问题

给定一个 `n` 个元素的数组，找到其中的主要元素。主要元素是指出现超过过 `[n/3]` 次的元素。*这个题目和第 169 题基本一样。*

**注意：**尝试在线性时间复杂度和常数空间复杂度内实现这个题的解答方案。

**例子：**

```
Input: [3,2,3]
Output: [3]

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```

## 思路

设置一个字典存储元素出现的次数，剩下的就无需赘言了。

## 答案

```python
class Solution:
    
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        d, l, res = {}, 0, []
        for num in nums:
            l += 1
            if str(num) in d: d[str(num)] += 1
            else: d[str(num)] = 1
        
        for idx, val in d.items():
            if val > l / 3: res.append(int(idx))
                
        return res
```