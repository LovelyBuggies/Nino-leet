# [67. Add Binary](https://leetcode.com/problems/add-binary/)

## 问题

给定两个二进制的字符串，返回它们的和。

输入的字符串应当既是非空的而且仅含有 0 和 1。

**例子：**

```
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
```

**限制：**

- 每个字符串中仅仅含有 `0` 和 `1`。
- `1 <= a.length, b.length <= 10^4`
- 每个字符串中要不然是 `0` 要不然就不含有无效的前置 `0`。

## 思路

同第 66 题类似，这个也是要从后往前遍历。只不过这个题需要确定一下有多少位。


## 答案

```python
class Solution:
    
    def addBinary(self, a: str, b: str) -> str:

        res = ''
        idx = carry = 0
        while idx < max(len(a), len(b)) or carry:
            aa = a[len(a)-1-idx] if idx < len(a) else '0'
            bb = b[len(b)-1-idx] if idx < len(b) else '0'
            
            carry, mod = divmod((int(aa) + int(bb) + carry), 2)
            res = str(mod) + res 
            idx += 1
        
        return res
```

一个比较 Pythonic 的方法是用 `eval()` 或者是 `bin` 函数。

```python 
class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
```

