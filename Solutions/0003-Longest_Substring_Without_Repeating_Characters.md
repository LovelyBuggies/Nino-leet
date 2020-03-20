# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 问题

给定一个字符串，在不重复字符的情况下找出最长的**子字符串**的长度。

**例子：**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

## 思路

这个题目要求找最长**子字符串**，而不是最长**子序列**。两者的区别在于：最长子序列找到是不重复的字符数目；最长子字符串还需要保证它们在原字符串中连在一起。

我们首先需要定义一个计数器和空字符串用来存储子字符串。然后遍历字符串中的字符：如果不存在就将这个字符添加到子字符串中；如果已经存在要添加的字符，就找到子字符串的该元素的位置，然后只取其后面的元素，并添加该元素；每次添加后都进行一次计数操作更新计数器。

## 答案

```python
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count, substr = 0, ""
        for ch in s:
            if ch in substr:
                substr = substr[substr.find(ch)+1:]
            substr += ch
            count = max(len(substr), count)
        
        return count   
```

