# 6. ZigZag Conversion

## 问题

字符串`"PAYPALISHIRING"`在给定行数上以ZigZag形式书写，如下所示：

```text
P   A   H    N
A P L S I I G
Y   I   R
```

然后一行一行地读：`"PAHNAPLSIIGYIR"`。

**例子：**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I     N
A   L S  I G
Y A   H R
P     I
```

## 思路

这个题目其实是一个索引游戏，我们首先需要搞清楚原字符串中每个元素在ZigZag中的位置。

```text
0                           2n-2                          4n-4
1                     2n-3  2n-1                      ·   4n-3
2                 ·         2n                   ·        4n-2
.            .               .              .              ·
.       n+1                 .           ·                  ·
n-2 n                       3n-4  3n-2                    5n-4
n-1                         3n-3                          5n-5
```

我们采用的方法是生成n行字符串，添加元素，再进行连接。我们发现其实每`2n-2`个元素其实是一个循环（周期）。循环中字符分布成两种类型的坐标：一种是在'Z'的竖边上；另一种是在'Z'的斜边上。

因为我们是从头开始遍历字符串中的元素，字符按照顺序添加到每一行（不存在之后的元素先被添加到某一行的情况），因此不需要考虑横坐标。在计算出字符索引关于周期的模之后，针对于上述两种情况，分别计算循环中的纵坐标：'Z'的竖边，在第`mod`行；'Z'的斜边，在第`period-mod`行。添加完元素连接就可以了。

## 答案

```python
class Solution:

    def convert(self, s: str, numRows: int) -> str:

        if numRows < 2:
            return s

        rows = ["" for i in range(numRows)]
        for idx, ch in enumerate(s):
            period = 2 * numRows - 2
            mod = idx % period
            if mod <= numRows - 1:
                rows[mod] += ch
            else:
                rows[period - mod] += ch

        return "".join(rows)
```

