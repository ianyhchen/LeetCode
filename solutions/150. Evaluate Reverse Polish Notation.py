class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []       
        operators = ["+", "-", "*", "/"]

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                # Pop the second operand first (order matters for - and /)
                num2 = stack.pop()
                # Pop the first operand
                num1 = stack.pop()

                if i == "+":
                    stack.append(num1 + num2)
                elif i == "-":
                    stack.append(num1 - num2)
                elif i == "*":
                    stack.append(num1 * num2)
                elif i == "/":
                    # In Python, 'int(a / b)' truncates toward zero, 
                    # whereas 'a // b' floors toward negative infinity, e.g. 6 // -132 = -1.
                    stack.append(int(num1 / num2))
        
        return stack[0] 
