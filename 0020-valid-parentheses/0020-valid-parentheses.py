class Solution:
    def isValid(self, s: str) -> bool:

        # APPROACH: Stack + HashMap
        # - Map every closing bracket to its matching opening bracket
        # - Push opening brackets onto the stack
        # - When we see a closing bracket, check if it matches the top of the stack
        # - Edge cases handled automatically:
        #   - Starts with closing bracket → stack is empty → return False
        #   - Unclosed opening brackets → stack is non-empty at end → return False

        stack = []
        closeToOpen = { "}":"{", "]":"[", ")":"("}

        for c in s:
            if c in closeToOpen:  # it's a closing bracket
                if stack and stack[-1] == closeToOpen[c]:  # top of stack must match the expected open bracket
                    stack.pop()  # valid pair, remove it
                else:
                    return False  # mismatch or empty stack (no opening bracket to pair with)
            else:
                stack.append(c)  # it's an opening bracket, save it for later matching
        
        return not stack  # valid only if every opening bracket was matched and popped


        