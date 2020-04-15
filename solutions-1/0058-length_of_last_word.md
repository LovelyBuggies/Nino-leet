# [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

## 问题

给定一个字符串 s 由大写/小写字母和空格字符 `' '` 组成，返回字符串中最后一个词的长度（如果从左到右循环，最后一个单词表示最后出现的单词）。

如果最后一个单词不存在，则返回 0。

**注意：**

一个词的定义是一个由非空格字符组成的**最大子字符串**。

**例子：**

```
Input: "Hello World"
Output: 5
```

## 思路

我们可以用一个比较 Pythonic 的方案来解决。值得注意的是，从右往左遍历（ `rstrip()` 和 `rsplit()` ）可以略微减少一些运行时间。


## 答案

```python
class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:
        
        return len(s.rstrip().rsplit(' ')[-1])
```