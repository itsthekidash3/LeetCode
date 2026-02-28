class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # APPROACH: Single Stack (Postfix evaluation)
        # - Postfix (Reverse Polish Notation) means operators come AFTER their operands
        # - Push numbers onto the stack
        # - When we hit an operator, pop the top TWO numbers, apply the operator, push result back
        # - ORDER MATTERS for - and /: second popped is the LEFT operand, first popped is RIGHT
        #   e.g. "3 4 -" means 3-4, so pop 4 (a) then pop 3 (b), compute b-a

        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())  # order doesn't matter for addition
            elif c == '-':
                a, b = stack.pop(), stack.pop()  # a = right operand, b = left operand
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())  # order doesn't matter for multiplication
            elif c == '/':
                a, b = stack.pop(), stack.pop()  # a = right operand, b = left operand
                stack.append(int(b / a))          # int() truncates toward zero (not floor division)
            else:
                stack.append(int(c))  # it's a number, push it
        
        return stack[0]  # final result is the only element left