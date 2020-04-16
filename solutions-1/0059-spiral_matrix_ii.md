# [59. Sprial Matrix II](https://leetcode.com/problems/spiral-matrix/)

## 问题

给定一个正整数 n，以螺旋的顺序构建一个从 1 到 n^2 的矩阵。

**例子：**

```
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Input: 6
Output:
[
 [1,2,3,4,5,6],
 [20,21,22,23,24,7],
 [19,32,33,34,25,8],
 [18,31,36,35,26,9],
 [17,30,29,28,27,10],
 [16,15,14,13,12,11]
]
```

## 思路

这个题目是第 54 题的逆操作，依然要用到递归。核心思路是：

- 首先，我们需要创建一个 n\*n 的矩阵。
- 递归中，我们用接下来的数字填充第一行，把它剩下的部分旋转并且传到下一层递归，这是为了让下次递归填充的第一行是我们的矩阵边。将得到的填充后再次旋转到正常方向。
- 初始化递归函数，设置递归终止条件。

## 答案

```python
import numpy as np

class Solution:
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        def generateMatrix(start, matrix):
            
            end = start + len(matrix[0])
            matrix[0] = [i for i in range(start, end)]
            
            if len(matrix) != 1: matrix[1:] = np.transpose(np.flip(generateMatrix(end, np.transpose(np.flip(matrix[1:], 0))), 0))
                
            return matrix
        
        return generateMatrix(1, [[0 for i in range(n)] for j in range(n)])
```

这是一个可读性比较好的解决方案，你也可以用 `zip()` 和 `[::-1]` 来旋转矩阵，这样会快点，但是可读性不是很好而且 `zip()` 返回数据类型的处理比较麻烦。

如果你比较丧心病狂，想要找到最短的解决方案，其实 2 行就可以了，但是可读性极差哦，而且反而会更慢。 :)

```python
class Solution:   
    def generateMatrix(self, n: int) -> List[List[int]]:
        def generateMatrix(start, matrix): return [[i for i in range(start, start + len(matrix[0]))]] + [list(i) for i in [*zip(*generateMatrix(start + len(matrix[0]), [*zip(*matrix[1:][::-1])])[::-1])]] if len(matrix) > 1 else [[i for i in range(start, start + len(matrix[0]))]]
        return generateMatrix(1, [[0 for i in range(n)] for j in range(n)])
```

