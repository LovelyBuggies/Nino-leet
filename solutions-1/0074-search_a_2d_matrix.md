# [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

## 问题

写一个高效的程序来寻找 m \* n 矩阵中的一个元素。矩阵中的元素是排好序的。

**例子：**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

## 思路

这个题目我们可以直接用一层循环 `for row in matrix: if target in row: return True`；或者用 numpy 来 `return target in {*numpy.array(matrix).ravel()}` 拍平（或者resize）查找一下（但这个很慢）。其实，这两种方法复杂度都是 O(n\*n)。为了降一下复杂度（然而并不能降多少 runtime），我们可以用两层二分查找。


## 答案

```python
class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]: return False
        
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < matrix[mid][0]: high = mid - 1
            else: low = mid + 1
        
        row = matrix[high]
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == row[mid]: return True
            elif target < row[mid]: high = mid - 1
            else: low = mid + 1
        
        return False
```