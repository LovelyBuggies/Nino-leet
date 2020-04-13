# [11. Container with Most Water](https://leetcode.com/problems/container-with-most-water/)

## 问题

给定一个长度为n的列表。用列表任意两个元素作边，构成一个容器。可以盛下的最多的水有多少单位？

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

*上述垂直线由列表`[1,8,6,2,5,4,8,3,7]`表示。在这种情况下，容器所能容纳的最大水面积（蓝色部分）是49。*

**注意：**容器不能倾斜，n最小为2，问题模型遵循**短板效应**。

**例子：**

```
**Input:** [1,8,6,2,5,4,8,3,7]
**Output:** 49
```

## 思路

这个题目有一个很直观的O(n^2)解法，两层循环，分别找左右两边，然后找water的最大值，如下所示：

```python
class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        
        contain = 0
        for l, left in enumerate(height):
            for r, right in enumerate(height[l+1:]):
                contain = max(contain, (r + 1) * min(left, right))
                
        return contain
```

这个代码虽然比较clean，甚至可以两行就解决，但是但是这个题的有趣之处在于，LeetCode OJ不允许O(n^2)解决，会出现"Time Limit Exceeded"。这迫使我们寻找O(n)的方案。

新算法的核心思路就是：

- 最宽的容器（使用头尾元素作为左右两边）是一个很好的选择，因为它很宽。它的水位是头尾元素中较小的一条的高度。
- 所有其他容器的宽度较小，因此需要更高的水位来容纳更多的水。
- 头尾元素中较小的不支持更高的水位，可以从进一步的考虑中移除。

有一个问题就是，如果两边恰好相等呢？这时候两者都是短板，朝向任何方向变更都是用短板长度（这两边的长度）来装水，所以本质上更新谁都是一样的。

## 答案

```python
class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        water = 0
        while l < r:
            water = max(water, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water
```

