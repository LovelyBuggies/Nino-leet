# [65. Valid Number](https://leetcode.com/problems/valid-number/)

## 问题

给定一个字符串，判断它是否能够被翻译成一个十进制的数字。

**例子：**

```
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
```

这个题目的陈述本身不是很清晰，是为了收集所有的需求。然而，一些合法的字符应当包含：

- 数字 0 - 9
- 指数 'e/E'
- 正负号 '+/-'
- 小数点 '.'

## 思路

这个题目最直观的方法是用正则表达式。根据应当包含中的项目，我们发现十进制的数字主要有三类：整数、小数、指数。其中，小数也可以表示为特殊的整数，指数的底可以是小数（但是幂必须是整数，比如 `1e6.5` 是不合法的）。所以我们还是分治一下，先考虑怎么构造合法的小数正则表达式`re_float = re_sign + '\d+[.]?\d*'` 或者 `re_float = re_sign + '\d*[.]?\d+'`，再套到指数正则表达式中 `re_exp = re_float + '[e|E]' + sign + '\d+'`。然后最后判断一下是否可以被其中一种正则匹配：`re_float + '$|' + re_exp + '$'` 。值得注意的是，一定要加上结尾判断符 `'$'`，不然 Python 的正则表达式会匹配一个空字符然后返回 True。

## 答案

```python
class Solution:
    
    def isNumber(self, s: str) -> bool:
        
        re_sign   = '[+|-]?'
        re_float1 = re_sign + '\d*[.]?\d+'
        re_float2 = re_sign + '\d+[.]?\d*'
        re_exp1   = re_float1 + '[e|E]' + re_sign + '\d+'
        re_exp2   = re_float2 + '[e|E]' + re_sign + '\d+'
        reg = re_float1 + '$|' + re_float2 + '$|' + re_exp1 +'$|' + re_exp2 + '$'
        
        return True if re.match(reg, s.strip()) else False
```

OR crazy (unreadable) one-line solution. :D

```python
class Solution:
    
    def isNumber(self, s: str) -> bool:
        
        return True if re.match(r'[+|-]?\d*[.]?\d+$|[+|-]?\d+[.]?\d*$|[+|-]?\d*[.]?\d+[e|E][+|-]?\d+$|[+|-]?\d+[.]?\d*[e|E][+|-]?\d+$', s.strip()) else False
```

