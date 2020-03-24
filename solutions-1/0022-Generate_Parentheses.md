# [22. Generate Parenthesis](https://leetcode.com/problems/generate-parentheses/)

## 问题

给定n对括号，编写一个函数来生成所有形式正确的括号组合。

例如，给定n = 3，解集为:

**例子：**

```markdown
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## 思路

组成正确括号组需要满足的条件是：任何一个位置，闭括号的数目要大于等于开括号。首先，我们先来看一种陷阱解法：

```python
class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        if n == 1:  return ['()']
        for s in self.generateParenthesis(n - 1):
            result += [str('(' + s + ')'), str('()' + s), str(s + '()')]
        
        return sorted(list(set(result)))
```

这个算法的思路是，对上一次递归的结果进行"前括" `'()' + s`，"中括" `'(' + s + ')'`，"后括" `s + '()'`，然后最后进行去重和排序。乍一看好像没有什么问题，但是当`n>=4`的时候，问题就出现了，有些情况比如`n=4` 时， `'(())(())'` 被遗漏了。为什么它被遗漏了呢？因为它"中括"的对象 `'())(()'` ——实际是不合法的！导致这种算法少考虑情况的核心原因是，"上一次递归结果合法"是"闭括号的数目要大于等于开括号"的充分不必要条件（上一次递归没有充分利用这一次递归的开闭括号数目条件）！

正确的做法是，将开闭括号数目条件作为一个类似于全局的变量传入到递归中，并按条件进行字符串创作：当还有开括号时，可以增加；当闭括号用的比开括号少时，可以增加；当不剩括号时，将字符串直接作为一种结果。最后返回起始递归。这种方法能避免上面的操作的问题的原因是：我们新定义的递归函数时刻"记忆"着用了多少开、闭括号，这样就能避免因为上面出现的遗漏情况。

## 答案

```python
class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(s: str, open: int, close: int, parens=[]) -> List[str]:
            
            if open:            generate(s + '(', open - 1, close)
            if close > open:    generate(s + ')', open, close - 1)
            if not close:       parens += [s]
            return parens
            
        return generate('', n, n)
```

