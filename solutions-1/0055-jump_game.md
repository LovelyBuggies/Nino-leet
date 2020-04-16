# [55. Jump Game](https://leetcode.com/problems/jump-game/)

## 问题

给定一个非负数组，假如一开始你位于数组的第一个索引处。数组中的每一个元素表示你在该位置的最大跳跃距离，判断一下你是否能到达最后一个索引处。

**例子：**

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

## 思路

这是一个经典的动态规划问题。核心思想就是得到在每一个索引（除了最后一个）的最大可达位置并更新最远可达距离。当索引值超过了最远可达距离，则返回无法抵达。遍历完成时，此时索引值还没有超过最远可达距离，则返回可以抵达。

## 答案

```python
class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        
        reach = 0
        for idx, num in enumerate(nums[:-1]):
            # the farthest reach
            reach = max(reach, idx + num)
            # if walk outreach the reach scope, return false
            if not idx < reach: return False
            
        return True
```