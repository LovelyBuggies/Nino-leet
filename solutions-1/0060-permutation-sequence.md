# [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

## 问题

集合 `[1,2,3...n]` 包含 n! 个独特的全排列。将所有排列按顺序排列并标记，得到 n = 3 的序列如下：

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

给定 n 和 k，返回第 k 个全排列序列。

**注意：**

- n 的范围从 1 到 9。
- k 的范围从 1 到 n!。

**例子：**

```
Input: n = 3, k = 3
Output: "213"

Input: n = 4, k = 9
Output: "2314"
```

## 思路

和第 46、47 类似，我们也可以借助 `itertools`，不过要处理一下输出的格式。


## 答案

```python
import itertools

class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        
        p = list(itertools.permutations([i for i in range(1, n+1)]))
        
        return ''.join([str(i) for i in list(p[k-1])])
        
        # oneline solution
        # return ''.join([str(i) for i in list(list(itertools.permutations([i for i in range(1, n+1)]))[k-1])])
```