# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## 问题

罗马数字由七个不同的符号表示：`I`、 `V`、 `X`、 `L`、 `C`、 `D` 和 `M`。

```markdown
Symbol        Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如，2用罗马数字写成`II`，两个1相加。12被写成`XII`，就是`X + II`。27这个数字被写成`XXVII`，也就是`XX + V + II`。

罗马数字通常是从左到右由大到小书写的。然而，数字4不是`IIII`。相反，数字4被写成`IV`，因为1在5之前，我们减去它得到4。同样的原则也适用于数字9，即`IX`。有六种情况下使用减法：

- `I`可以放在`V`和`X`前面，得到4和9。
- `X`可以放在`L`和`C`前面，得到40和90。
- `C`可以放在`D`和`M`之前，得到400和900。

给定一个罗马数字字符串，把它转化成整数。输入保证在1到3999之间。

**例子：**

```markdown
Input: "III"
Output: 3

Input: "IV"
Output: 4

Input: "IX"
Output: 9

Input: "LVIII"
Output: 58

Input: "MCMXCIV"
Output: 1994
```

## 思路

首先，我们先不考虑6种减法特殊情况。不断进行一个高位（这里的位是指`M`、`D`、`C` …）读取的操作`s[idx]`，然后对结果进行累加就好了。

对于那6种特殊情况的减法，我们需要预先判断每个字符后面的字符是否和它一起构成一个数字。当然，最后一位就不需要判断了，因为没有下一位。

## 答案

```python
class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        d = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}

        result, idx = 0, 0
        while idx < len(s):
            if idx != len(s) - 1:
                if s[idx] + s[idx+1] in d:
                    result += d[s[idx] + s[idx+1]]
                    idx += 1
                else:
                    result += d[s[idx]]
            else:
                result += d[s[idx]]
            idx +=1
             
        return result
```

