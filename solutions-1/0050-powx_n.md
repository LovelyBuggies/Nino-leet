# [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

## 问题

实现 `pow(x, n)` 计算 x 的 n 次方。

**注意：**

- -100.0 < 100.0
- n 的范围在 [-2^31, 2^31 - 1] 之间。

**例子：**

```
Input: 2.00000, 10
Output: 1024.00000

Input: 2.10000, 3
Output: 9.26100

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

## 思路

这个题就比较无聊，没有说我们需要 focus 的点，递归迭代都可以。


## 答案

```python
class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        
        return pow(x, n)
```