# [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## 问题

给定一个链表，删除其中所有**重复过**的元素，保证只有**曾经**独一无二的元素留在原链表中。

返回结果依然保持有序状态。

**例子：**

```
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Input: 1->1->1->2->3
Output: 2->3
```

## 思路

当用 Python 一切变得很简单。我们可以尝试用 Python 内置的函数 `index()`（ `index()` 和 `find()` 有区别的，`find()` 找不到会返回 -1，但它不能用于list）。只需要两行代码就可以轻松搞定：

```python
if target not in nums:  return -1
else:   return nums.index(target)
```

同第 33 题一样，我们可以用一种类似于二分查找的方法，分别确定最大最小元素的 index 就可以当成一个真正的有序数列来处理了。

## 答案

```python
class Solution:
    
    def search(self, nums: List[int], target: int) -> bool:
        
        if not len(nums): return False
        
        # 查找最大最小元素
        high, l = 0, len(nums)
        while high < l - 1:
            if nums[high+1] < nums[high]: break
            else: high += 1
        
        # 二分查找
        low = high - l + 1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]: high = mid - 1
            elif target > nums[mid]: low = mid + 1
            else: return True

        return False       
```
