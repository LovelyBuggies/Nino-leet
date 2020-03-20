# 8. String to Integer \(atoi\)

## 问题

实现一个`atoi`函数，将字符串转化成一个整数。

该函数首先丢弃尽可能多的空白字符，直到找到第一个非空白字符。然后，从这个字符开始，取一个可选的初始加号或减号，后面跟尽可能多的数字，并将它们解释为一个数值。

字符串可以包含构成整数的字符之后的其他字符，这些字符将被忽略，并且对该函数的行为没有影响。

如果str中的第一个非空白字符序列不是有效的整数，或者由于str为空或它只包含空白字符而不存在这样的序列，则不执行转换。

如果不能执行有效的转换，则返回零值。

**注意:**

* 只有空格字符`' '`被认为是空白字符。
* 假设我们处理的环境只能存储32位带符号整数范围内的整数：\[−2^31,2^31−1\]。如果数值超出了可表示值的范围，则返回`INT_MAX=2^31−1`或`INT_MIN=−2^31`。

**例子：**

```text
**Input:** "123"
**Output:** 123

**Input:** "-123"
**Output:** -123

**Input:** "123 with words"
**Output:** 123

**Input:** "words and 123"
**Output:** 0
```

## 思路

这个题目我们可以用正则表达试来避免众多复杂的`if ... else ..`。字符串中的敏感字符包括：`+`、`-`、`0`，及数字`0~9`。移除掉字符串首尾空字符之后，我们查找这些敏感字符，并根据正则表达式的含义限定捕获子序列的条件。最后判定是否溢出。

## 答案

```python
import math, re

class Solution:

    def myAtoi(self, str: str) -> int:

        numberStr = re.findall('^[\+\-]?0*\d+', str.strip())

        if numberStr:
            num = int(numberStr[0])
            if num < -math.pow(2, 31):
                return int(-math.pow(2, 31))
            elif num > math.pow(2, 31) - 1:
                return int(math.pow(2, 31) - 1)
            else:
                return int(num)
        else:
            return 0
```

