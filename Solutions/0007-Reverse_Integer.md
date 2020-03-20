# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

## 问题

给定一个32位带符号整数，对其进行反转运算。

**例子：**

```markdown
**Input:** 123
**Output:** 321

**Input:** -123
**Output:** -321

**Input:** 120
**Output:** 21
```

## 思路

对于一个常规数，从低到高位取模提取每一位数字（`x%10`），早提取出来的进行升位操作（`res*10`）即可。对于负数，因为取模是反的，所以我们单独处理符号位。对于超过范围的数或者0，返回0（*值得注意的是，有可能输入数没有越界，而结果溢出，所以保险的做法是在返回时判断*）。

## 答案

```python
class Solution:
    
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        res = 0
        a = x / abs(x)
        x = abs(x)
        while x > 0:
            res = 10 * res + x % 10
            x = int(x / 10)
            
        return int(a * res) if a * res > -math.pow(2, 31) and a * res < math.pow(2, 31) - 1 else 0
```

