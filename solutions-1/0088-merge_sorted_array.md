# [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

## 问题

给定两个整数数组 `nums1` 和 `nums2 `，合并 `nums2` 到 `nums1 ` 。

**注意：**

- `nums1` 和 `nums2` 中初始化的元素个数分别为 m 和 n。
- 可以假设 `nums1` 有足够的空间（大小大于或等于m + n）来容纳 `nums2` 中的其他元素。

**例子：**

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

## 思路

切片切一下，然后重排就好了。

## 答案

```python
class Solution:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[:] = sorted(nums1[:m] + nums2[:n])
```
