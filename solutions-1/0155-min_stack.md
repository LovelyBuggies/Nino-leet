# [155. Min Stack](https://leetcode.com/problems/min-stack/)

## 问题

设计一个栈支持 `push` 、 `pop` 、 `top` 、 `getMin` 的操作。

- `push`：元素入栈。
- `pop`：元素出栈。
- `top`：栈顶元素。
- `getMin`：栈中最小值。

**例子：**

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## 思路

这个题目比较简单，不多赘述了。

## 答案

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = []

        
    def push(self, x: int) -> None:
        
        self.stack.append(x)

        
    def pop(self) -> None:
        
        self.stack.pop()

        
    def top(self) -> int:
        
        return self.stack[-1]
    

    def getMin(self) -> int:
        
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```