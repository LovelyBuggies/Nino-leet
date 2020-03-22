# [20. Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/)

## 问题

给定一个只包含字符`'('`，`')'`，`'{'`，`'}'`，`'['`和`']'`的字符串，判断输入字符串是否有效。

输入字符串是有效的，如果:

- 开括号必须由相同类型的闭括号括起。

- 开括号必须按正确的顺序闭合。

注意，空字符串也被认为是有效的。

**例子：**

```markdown
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
```

## 思路

一种直观的做法就是用栈（或者类似思路）的push和pop进行操作。但是其实有一种更简单的聪明做法 :-)，直接在字符串中remove掉pairs就好了。

## 答案

```python
class Solution:
    
    def isValid(self, s: str) -> bool:
        
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return not len(s)
```

