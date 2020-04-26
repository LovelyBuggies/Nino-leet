# [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## 问题

**斐波那契数列**通常表示 `F(n)` 组成一个序列，每个数字都是前两个数字的和，从 `0` 和 `1 `开始。

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
```

给定一个整数 `N`，计算 `F(N)`

**例子：**

```
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

**注意：**

0 ≤ `N` ≤ 30。

## 思路

同第 70 题类似，这个题我们也不能用递归，遇到大数 n 的时候可能会 Time Limit Exceeded。我们可以用两个变量分别记住 Fibonacci 数列中的前两个数，然后不断更新这两个变量就好了。

## 答案

```python
class Solution:
    
    def fib(self, N: int) -> int:
        
        if not N: return 0
        
        a, b = 0, 1
        for i in range(N - 1):
            a, b = b, a + b
            
        return b
```