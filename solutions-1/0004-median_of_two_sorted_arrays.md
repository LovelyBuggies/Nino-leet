# 4. Median of Two Sorted Arrays

## 问题

有两个大小分别为m和n的排序数组nums1和nums2。

求两个排序数组的中位数。总的运行时复杂度应该是O\(log \(m+n\)\)。

可以假设nums1和nums2不能同时为空。

**例子：**

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

## 思路

将两个list合并并升序重排，然后找中位数就好了。这个其实一行代码可以搞定，但是为了代码的可读性和少一些内存，我将答案拆分成三行。

## 答案

```python
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = sorted(nums1+nums2)
        div, mod = divmod(len(nums), 2)
        return nums[div] if mod else (nums[div-1] + nums[div])/2
```

