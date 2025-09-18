# Last updated: 9/17/2025, 6:08:35 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        
        
        for i in range(len(tokens)):

            if tokens[i] == "+":
                stack.append(stack.pop()+stack.pop())
            elif tokens[i] == "-":
                second,first = stack.pop(),stack.pop()
                stack.append(first-second)      
            elif tokens[i] == "/":
                second,first = stack.pop(),stack.pop()
                stack.append(int(first/second))      
            elif tokens[i] == "*":
                stack.append(stack.pop()*stack.pop())     
            else:
                stack.append(int(tokens[i]))
        return stack[0]

        