# [46. Permutations II](https://leetcode.com/problems/rotate-image/)

## 问题

给定一组整数（可能存在重复数），返回所有可能的不重复排列（非重全排列）。

**例子：**

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

## 思路

Python 的常用内建模块 `itertools` 有对 `permutations()` 的良好封装，就没必要劳神苦思了。当然你也可以从它的[源码](https://github.com/python/cpython/blob/master/Modules/itertoolsmodule.c)看它是怎么实现的。最后我们进行一个去重操作就可以了。


## 答案

```python
import itertools

class Solution:
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        return list(set(itertools.permutations(nums)))
```