# Last updated: 9/17/2025, 6:08:17 PM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":

                stack.append(char)
            else:
                curr = ""
                while stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()

                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                
                curr = int(curr_num) * curr

                stack.append(curr)

        return "".join(stack)



        