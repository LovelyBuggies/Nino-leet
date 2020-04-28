# [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)

## 问题

给定一个数 n，有多少个存储 1 到 n 的不重复的二叉搜索树。

**例子：**

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

## 思路

对于 n 个节点的二叉搜索树，我们可以选择 1 到 n 任意一个数字作为根节点的值，比如 i。那么，跟节点的左边就是 1 到 i - 1 构成的二叉搜索树；跟节点的右边就是 i + 1 到 n 构成的二叉搜索树。如果用 F(n) 表示n 个节点的非重二叉搜索树个数，那么 F(n) 应该等于 `F(i-1)*F(n-i)` 。于是，我们就可以用递归实现了。

```python
class Solution:
    
    def numTrees(self, n: int) -> int:
        
        if n == 0: return 1
        
        res = 0
        for i in range(1, n+1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        
        return res
```

然而，这种递归问题总是伴随着运行时间超时的问题，我们只好把它改成一个动态规划的解决形式。因为非重二叉搜索树个数只跟节点数有关，换句话说，1 到 3 的非重二叉搜索树个数和 2 到 4 的非重二叉搜索树个数是一样的。所以，我们可以维护一个数组，来分别记录多少个节点可以生成多少棵树。

*值得注意的是，因为 n 个节点生成二叉搜索树会用到 1 到 n 所有数量可以生成的二叉搜索树，所以我们必须用一个数组来维护，而不能单单记录几个变量像 Fibonacci 数列那样。*

## 答案

```python
class Solution:
    
    def numTrees(self, n: int) -> int:
        
        arr = [1] + [0] * n
        for i in range(1, n+1):
            for j in range(1, i+1):
                arr[i] += arr[j-1] * arr[i-j]
        
        return arr[-1]
```

*Btw，这种数叫做 [Catalan 数](http://en.wikipedia.org/wiki/Catalan_number)。*