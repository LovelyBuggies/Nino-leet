# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

## 问题

给定一个 m\*n 的矩阵，如果其中某一元素为 0，将其同行或者同列的元素都设置为 0。

**例子：**

```
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

**跟进：**

- 一个很直观的思路就是用 O(mn) 的空间，这是一个不好的方法。
- 一个简单的提升是用 O(m + n) 的空间，然而这依然不是最好的方法。
- 你能设计一个常数空间的解决方案么？

## 思路

"跟进"中说了希望我们用一个常数空间的解决方案，于是我们可以用 O(1) 的字典，将 0 的横纵坐标元组作为键存进去，然后再 set 0 就好了。


## 答案

```python
class Solution:
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        idxs = {}
        
        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                if col == 0: idxs[(r, c)] = 0
        
        for idx_r, idx_c in idxs.keys():
            for c in range(len(matrix[0])): matrix[idx_r][c] = 0
            for r in range(len(matrix)): matrix[r][idx_c] = 0
```