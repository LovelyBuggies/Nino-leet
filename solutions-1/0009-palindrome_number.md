# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## 问题

确定一个整数是否是回文。当一个整数向后和向前读取相同的内容时，它就是一个回文数。

**例子：**

```
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## 思路

这个题目比较简单，只需要根据回文数定义判断就好了。

另外，我们也可以用一种比较 Pythonic 的解决方案。

## 答案

```python
# 定义方法
class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        s = str(x)
        for idx in range(len(s) // 2):
            if s[idx] != s[-idx-1]: return False
        
        return True
      
# Pythonic 方法
class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        return str(x)[::-1] == str(x) and not x < 0
```
