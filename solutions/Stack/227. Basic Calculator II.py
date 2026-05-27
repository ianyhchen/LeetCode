class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        last_op = "+"
        current_num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                current_num = current_num * 10 + int(c)

            # c is operator or the tail of s
            if c in "+-*/" or i == len(s) - 1:
                if last_op == "+":
                    num_stack.append(current_num)
                elif last_op == "-":
                    num_stack.append(-current_num)
                elif last_op == "*":
                    top_num = num_stack.pop()
                    num_stack.append(top_num * current_num)
                elif last_op == "/":
                    top_num = num_stack.pop()
                    num_stack.append(int(top_num / current_num))

                if c in "+-*/":
                    last_op = c
                current_num = 0

        return sum(num_stack)

# Non stack solution
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        total_sum, current_num, last_num = 0, 0, 0
        last_op = "+"
        current_num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                current_num = current_num * 10 + int(c)

            # c is operator or the tail of s
            if c in "+-*/" or i == len(s) - 1:
                if last_op == "+":
                    # Add previous confirmed last_item to total and start new chain
                    total_sum += last_num
                    last_num = current_num
                elif last_op == "-":
                    # Add previous confirmed last_item to total and start new negative chain
                    total_sum += last_num
                    last_num = -current_num
                elif last_op == "*":
                    # Update current chain directly
                    last_num = last_num * current_num                   
                elif last_op == "/":
                    # Update current chain directly with toward-zero division
                    last_num = int(last_num / current_num)                                      

                if c in "+-*/":
                    last_op = c
                current_num = 0

        # Add the final buffer item to total_sum
        return total_sum + last_num