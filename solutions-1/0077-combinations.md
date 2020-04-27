# [77. Combinations](https://leetcode.com/problems/combinations/)

## 问题

给定两个数 n 和 k，返回从 1 到 n 所有的组合 k 数。

**例子：**

```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

## 思路

同第 46 题类似，我们可以用 [itertools](https://github.com/python/cpython/blob/master/Modules/itertoolsmodule.c) 的轮子。


## 答案

```python
import itertools

class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        return itertools.combinations([i for i in range(1, n+1)], k)
```