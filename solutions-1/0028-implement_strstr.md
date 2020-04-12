# [28. Implement strstr()](https://leetcode.com/problems/implement-strstr/)

## 问题

实现`strStr()`方法（C库函数）。

返回`haystack`中第一次出现`needle`的索引，如果`needle`不是`haystack`的一部分，则返回 **-1**。

**例子：**

```markdown
Input: haystack = "hello", needle = "ll"
Output: 2

haystack = "aaaaa", needle = "bba"
Output: -1
```

**澄清：**

如果`needle`是一个空字符串，我们该返回什么呢？这是面试常问的问题。

在这个问题中，当`needle`是一个空字符串时我们返回0。实际上C语言的`strstr()`和Java的`indexOf()`是这么处理的。

## 思路

当用Python，一切就会变得很简单。 :)

## 答案

```python
class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        
        return -1 if needle not in haystack else haystack.index(needle)
```

