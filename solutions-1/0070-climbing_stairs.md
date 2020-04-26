# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

## 问题

假设你每次可以爬 1 或 2 阶台阶，你有多少种不同爬法来爬 n 阶台阶？假设 n 为正。

**例子：**

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## 思路

这个题目其实就是一个斐波拉契数列。假设你在第 n 阶（n > 2）台阶，你是怎么爬到这里的？一种方法就是从第 n-1 阶台阶上爬了一阶上来的；另一种方法是从第 n-2 阶台阶上爬了两阶上来的，所以爬到第 n 阶的方法种类等于爬到第 n-1 阶台阶和爬到第 n-2 阶台阶的方法种类之和。

但是，这个题不能用递归哦，遇到摩天大阶的时候可能会 Time Limit Exceeded。那我们该怎么办呢？第一个办法就是维护一个 list，其中存储每一阶台阶的爬法种类。但是，这个其实还是蛮烧内存的。假如我想想爬到第 1000 阶台阶，我得需要一个长度为 1000 的 list，我没必要记住第 100 阶的爬法种类，我只需要记住 n-1 和 n-2 阶的爬法种类就行了。所以我们可以用两个变量分别记住  n-1 和 n-2 阶的爬法种类，然后不断更新这两个变量就好了。


## 答案

```python
class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
            
        return a
```