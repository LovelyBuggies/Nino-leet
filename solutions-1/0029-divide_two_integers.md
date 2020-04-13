# [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

## 问题

有两个整数 `dividend` 和 `divisor` ，**不用**乘法、除法和取模运算符的情况下将两个整数整除，并返回它们的商。整数除法应该从零截断，这意味着丢失小数部分。比如，`truncate(8.345) = 8` 和 `truncate(-2.7335) = -2`。

**例子：**

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
```

**注意：**

- 被除数和除数都是32位有符号整数。
- 除数永远不会是0。
- 假设我们处理的环境只能存储32位带符号整数范围内的整数:[−2^31, 2^31 − 1]。对于这个问题，假设你的函数在除法结果溢出时返回2^31 - 1。

## 思路

这个题目其实可以直接通过

 ```python
return min(max(-2147483648, int(dividend / divisor)), 2147483647)
 ```


来 AC。但是毕竟题目说了"不用乘法、除法和取模运算符的情况下将两个整数整除"，我们还是应当给予这个 Medium 难度的题目一点尊重。 :) 这个题目实际上想考察的是位运算中的 `<<` 和 `>>` 运算符。其中 `divisor << x` 得到的结果是 `divisor * (2^x)`；反之， `n >> d` 得到的结果是 `divisor / (2^x)` 。

比如当被除数等于 33，除数等于 5 的情况下，在确定符号之后，我们需要找到一个最大的 2 的倍数 — 2，使其与除数的积小于等于被除数。然后我们需要从 33 中剔除 `5 << 2` 也就是 20 的部分得到 13，并将这个左移位 2 加给结果。接下来，我们对 13 采用同样的操作，剔除掉 `5 << 1` 也就是10的部分得到3，并将这个左移位 1 加给结果。因为 `3 < 5`，我们不能够从中再剔除任何 2 的倍数与除数 5 的积，其实是忽略掉了 `33 / 5` 中 `3 / 5` 的部分。循环结束，结果就是 `2^2 + 2^1` （注意千万不能考虑成 `2^3`，因为两次移位的影响不是等价的）。最后做一下溢出处理就OK了。

当你用位操作实现了除法之后，一个很直观的想法就是如何用位操作实现乘法。相似的思路，对其中一个乘数不断的右移，找到最大右移位数使其移动后不为 0。然后从这个乘数中剔除这部分，给另一个乘数移动相同位数。以此类推，直到这个乘数"蜡炬成灰"。这个练习中，我将乘法和除法的答案都写了下来。

实际上，位操作运算的目的是为了加快运算速度，但这个算法的时间复杂度是 O(n^2)。而且从运行时间来看这种方法也不如上面的 trick。即使如此，掌握位操作的知识还是对我们有帮助的，也许大数运算会用到，或者作为茶余饭后的闲谈。

## 答案

```python
# 位操作实现除法
class Solution:
    
    def divide(self, dividend: int, divisor: int) -> int:
        
        sig = (dividend < 0) == (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            x = 0
            while dividend >= divisor << (x + 1): x += 1
            dividend -= divisor << x
            res += 1 << x
            
        return min(res if sig else -res, 2147483647)
      

# 位操作实现乘法
class Solution:
    
    def multiple(self, multiple1: int, multiple2: int) -> int:
        
        sig = (multiple1 < 0) == (multiple2 < 0)
        multiple1, multiple2, res = abs(multiple1), abs(multiple2), 0
        while multiple2 > 0:
            x = 0
            while multiple2 >> (x + 1): x += 1
            res += multiple1 << x
            multiple2 -= (1 << x)
            
        return min(res if sig else -res, 2147483647)
```

