# [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

## 问题

**Tribonacci 数列**通常表示 `T(n)` 组成一个序列，每个数字都是前三个数字的和，从 `0`、 `1`、`1` 开始。

```
T(0) = 0,   T(1) = 1,   T(2) = 1
T(N) = T(N - 1) + T(N - 2) + T(N - 3), for N > 1.
```

给定一个整数 `N`，计算 `T(N)`

**例子：**

```
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Input: n = 25
Output: 1389537
```

**注意：**

- 0 ≤ `N` ≤ 37。
- 答案应当在整数范围内，`answer <= 2^31 - 1`。

## 思路

同第 509 题类似，我们用三个变量分别记住 Tribonacci 数列中的前三个数，然后不断更新这三个变量就好了。

## 答案

```python
class Solution:
    
    def tribonacci(self, n: int) -> int:
        
        if not n: return 0
        
        a, b, c = 0, 0, 1
        
        for i in range(n - 1):
            a, b, c = b, c, a + b + c
            
        return c
```