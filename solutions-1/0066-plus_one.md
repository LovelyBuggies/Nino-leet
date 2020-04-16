# [66. Plus One](https://leetcode.com/problems/plus-one/)

## 问题

给定一个**非空**的数组，表示一个非负整数，用数组表示给它加 1 后的整数。

这些数字的存储方式是，最有效的数字位于列表的开头，数组中的每个元素都包含一个数字。

你可以假设整数不包含任何前导零，除了数字 0 本身。

**例子：**

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

## 思路

一种很简单的方式就是献给这个数末尾加上 1，然后再处理进位（然而一个比较不优雅的事情是索引，因为我们不能 `for digit in digits[::-1]` 地给 `digits` 中的元素赋值）。


## 答案

```python
class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry, digits[-1] = 0, digits[-1] + 1
        for idx, _ in enumerate(digits): carry, digits[-idx-1] = divmod(digits[-idx-1] + carry, 10)
            
        return digits if not carry else [1] + digits
```