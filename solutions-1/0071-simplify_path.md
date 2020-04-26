# [71. Simplify Path](https://leetcode.com/problems/simplify-path/)

## 问题

给定一个文件的**绝对路径**（Unix 风格的），尝试简化它成一个**规范路径**。

在 Unix 文件系统中，`.` 表示当前目录，`..` 表示上一层目录。

注意，返回的**规范路径**必须以 `/` 开头，并且两个目录之间必须有一个 `/`，并且最后不含有 `/` 。**规范路径**是最短的**绝对路径**。

**例子：**

```
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Input: "/a/./b/../../c/"
Output: "/c"

Input: "/a/../../b/../c//.//"
Output: "/c"

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
```

## 思路

这个题目虽然看起来很复杂，但是我们可以用栈的思路解决，最后输出的规范路径其实就是目录栈中的项目。首先，将输入的绝对路径中的目录分隔开：如果是 `'.'` 或者 `''`，这是无用字符；如果是 `..`，弹出栈顶元素；对于正常的目录名，将其入栈。最后给栈中的每个目录前加一个 `/` 就好了。


## 答案

```python
class Solution:
    
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        
        for p in path.split('/'):
            if p and p != '.' and p != '..': stack.append(p)
            elif p == '..' and stack: stack.pop()
            else: continue
                
        return '/' + '/'.join(stack)
```