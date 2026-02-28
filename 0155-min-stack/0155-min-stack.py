# CONSTANT TIME? Yes — all operations are O(1)
# KEY INSIGHT: a second "minStack" that tracks the minimum AT EVERY LEVEL of the stack
# so when you pop, you still know what the min was before that element was pushed

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []  # parallel stack — each position holds the min up to that point
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # the current min is either val itself, or whatever the previous min was
        # minStack[-1] always holds the running minimum before this push
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()  # both stacks stay in sync, so min history is preserved
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]  # top of minStack = minimum at the current stack state