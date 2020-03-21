# [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

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

罗马数字通常是从左到右由大到小书写的。然而，数字4不是`IIII``。相反，数字4被写成IV`，因为1在5之前，我们减去它得到4。同样的原则也适用于数字9，即`IX`。有六种情况下使用减法：

- `I`可以放在`V`和`X`前面，得到4和9。
- `X`可以放在`L`和`C`前面，得到40和90。
- `C`可以放在`D`和`M`之前，得到400和900。

给定一个整数，把它转换成罗马数字。输入保证在1到3999之间。

**例子：**

```markdown
Input: 3
Outpu "III"

Input: 4
Output: "IV"

Input: 8
Output: "IX"

Input: 58
Output: "LVIII"

Input: 1994
Output: "MCMXCIV"
```

## 思路

首先，我们先不考虑6种减法特殊情况。不断进行一个高位（这里的位是指`M`、`D`、`C` ...）提取的操作 `num / value`，然后找到对应的罗马字母就可以了。

对于那6种特殊情况的减法，如果剩余出来的模 `num % value` 恰好是其中一种，那么我们不再进行继续提取高位，直接用他们赋值就好了。

## 答案

```python
class Solution:
    
    def intToRoman(self, num: int) -> str:
        
        d = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        
        result = ""
        for k, v in d.items():
            result += k * int(num / v)
            num %= v
            
        return result
```

