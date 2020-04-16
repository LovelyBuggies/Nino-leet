# [48. Rotate Image](https://leetcode.com/problems/rotate-image/)

## 问题

用一个 n\*n 的 2D 矩阵表示一个图像，将图像顺时针旋转 90 度。

**注意：**

你必须旋转图像的位置，这意味着你必须直接（[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)）修改输入的 2D 矩阵，**不要**创建另一个 2D 矩阵。

**例子：**

```
Input: 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Output:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Input:
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

Output:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

## 思路

这个题目看起来跟是不是图片没有什么关系，就是让旋转 2-D 矩阵。旋转 2-D 矩阵的奥妙就在于，这个旋转操作其实是可以由反转和置换操作组合完成的。除了答案的做法，你也可以通过 Python 内置的 `list.reverse()` 和 `reversed()` 完成。当然，如果你引入了 `numpy` 包，你也可以用 `np.flip(matrix, 0)` 完成顺时针的旋转（ `np.flip(matrix, 1)` 完成逆时针旋转）。

*题外话：看起来 LeetCode 检查是否是 in-place 的策略是对输入的 matrix 进行检查，所以直接返回是没有用滴！*


## 答案

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        matrix[:] = zip(*matrix[::-1])
        
        return matrix
```