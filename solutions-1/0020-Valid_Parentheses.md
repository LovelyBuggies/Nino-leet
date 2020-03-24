# [20. Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/)

## 问题

给定一个只包含字符`'('`，`')'`，`'{'`，`'}'`，`'['`和`']'`的字符串，判断输入字符串是否有效。

输入字符串是有效的，如果：

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

一种直观的做法就是用栈的push和pop进行操作（或者用其他数据结构进行类似思路的操作）。对于开括号，进行入栈；对于闭括号，如果栈非空且匹配栈顶，则顶栈元素出栈；否则直接返回不合法。当然这个只适用于没有其他字符的字符串，如果含有其他字符，增加判定条件即可。

```python
class Solution:
    
    def isValid(self, s: str) -> bool:
        
        d = {'(':')', '[':']', '{':'}'}
        result = ''
        for p in s:
            if p in d.keys():
                result += p
            elif len(result) and {v:k for k, v in d.items()}[p] == result[-1]: # another elif: len(result) and [k for k, v in d.items() if v == p][0] == result[-1]
                result = result[:-1]
            else: return False
                
        return not len(result)
```

但是其实有一种更简单的聪明做法 : -)，直接在字符串中remove掉pairs就好了。

## 答案

```python
class Solution:
    
    def isValid(self, s: str) -> bool:
        
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return not len(s)
```

