# [46. Permutations](https://leetcode.com/problems/permutations/)

## 问题

给定一组**不同**的整数，返回所有可能的排列（全排列）。

**例子：**

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## 思路

Python 的常用内建模块 `itertools` 有对 `permutations()` 的良好封装，就没必要劳神苦思了。当然你也可以从它的[源码](https://github.com/python/cpython/blob/master/Modules/itertoolsmodule.c)看它是怎么实现的。


## 答案

```python
import itertools

class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return itertools.permutations(nums)
```