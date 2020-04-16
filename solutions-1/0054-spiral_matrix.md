# [54. Sprial Matrix](https://leetcode.com/problems/spiral-matrix/)

## 问题

给定一个 m \* n 的矩阵，以旋转的顺序返回所有元素。

**例子：**

```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## 思路

这个题目和第 48 题有异曲同工之妙。将矩阵旋转，不停提取第一行就好了。

答案中两个点值得注意：

- `[*]` 的效果和 `list()` 一样，都是为了将 tuple 转化成 list（因为 `zip()` 生成了 tuple），但是这种方法稍微快一点。
- 最后的返回 `return A and B` 将会在 B 不出错的情况下返回 B，否则返回 A。这个操作是为了终止递归。

另外你也许会好奇，为什么 48 题还需要两行，这个一行就可以了？因为这个题目是不需要 in-place 的，所以没必要再赋值给 matrix。 :)

## 答案

```python
class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
```