# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## 问题

给定一个长度为 n 的非负整数，表示一个高度图，其中每个条的宽度为 1，计算它在雨后能够捕获多少水。

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

*上述高度图由数组 `[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]` 表示。在这种情况下，6 个单位的雨水（蓝色部分）被捕获。*


**例子：**

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## 思路

这个题目和第 11 题很像，因此我们可以采取相同的思路，用一个头指针和尾指针进行一次 one-pass 迭代。每次循环，我们需要做三件事情。

- 改变头指针或尾指针的位置 — `l, r`：和 11 题一样，谁是短板就不要谁。
- 确定水位 — `level`：水位是短板和原先水位的最大值。
- 确定蓄水量 — `water`：蓄水量是水位减去短板（这也就是说，如果你的水位被更新成了短板，那么将不会蓄水；如果短板不如水位高，就会有蓄水）。

指针的

我们先看一个简单的例子，其中高度图由 `[3, X, 5]` 表示。


## 答案

```python
class Solution:
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        target = 1
        while target in nums:
            target += 1
            
        return target
```

