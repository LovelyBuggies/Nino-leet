# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## 问题

给定一个字符串数组，将颠倒字母而成的字进行分组。

**注意：**

- 所有输入的字符串都是小写的。
- 输出的顺序无关紧要。

**例子：**

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

## 思路

这个题目其实就是对含有相同字母的单词进行分组。用字典可以轻松实现，只不过字典的 key 实际上是一个由含有字母组成的元祖。


## 答案

```python
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for w in strs:
            chs = tuple(sorted(w))
            d[chs] = d.get(chs, []) + [w]
        # d = {('a', 'e', 't'): ['eat', 'tea', 'ate'], ('a', 'n', 't'): ['tan', 'nat'], ('a', 'b', 't'): ['bat']}
        
        return sorted(d.values())
```