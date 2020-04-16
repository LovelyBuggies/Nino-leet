# [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

## 问题

实现 `sqrt(x)` 计算 x 的平方根，其中 x 是非负数。小数位数被截断，只返回结果的整数部分。

**例子：**

```
Input: 4
Output: 2

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
```

## 思路

这个题就比较无聊，并没有说我们需要 focus 的点。


## 答案

```python
class Solution:
    
    def mySqrt(self, x: int) -> int:
        
        return int(sqrt(x))
```