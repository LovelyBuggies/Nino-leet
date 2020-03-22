# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## 问题

编写一个函数来查找字符串数组中最长的公共前缀字符串。

如果没有公共前缀，则返回空字符串“”。

**例子：**

```markdown
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## 思路

首先我们先要制定一个寻找两个字符串的公共前缀的方法，Python3没有封装好的这种方法，所以我们需要一层循环来实现。然后，不断比较、更新列表公共前缀即可。

## 答案

```python
class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        result = strs[0]
        for s in strs:
            idx = 0
            while idx < len(s):
                if s[:idx+1] == result[:idx+1]:
                    idx += 1
                else:
                    break
            result = s[:idx]
                    
        return result
```

