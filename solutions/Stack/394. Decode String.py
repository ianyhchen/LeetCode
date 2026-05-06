class Solution:
    def decodeString(self, s: str) -> str:
        # stack_k stores the repeat count k
        # stack_s stores the string prefix before the '['
        stack_k, stack_s = [], []
        res = ""
        k = 0
        for c in s:            
            if c.isdigit():
                # Handle multi-digit numbers (e.g., "100")
                k = k * 10 + int(c)
            elif c == '[':
                # Push the current multiplier and the string built so far onto stacks
                stack_k.append(k)
                stack_s.append(res)
                # Reset for the new context inside the brackets
                k = 0
                res = ""           
            elif c == ']':
                # Pop the last saved prefix and multiplier
                last_k = stack_k.pop()
                last_res = stack_s.pop()

                # Construct the decoded string for this level
                # current res is the content inside [], multiply it and attach to prefix
                res = last_res + last_k * res
            else:
                # Character is a letter, append to the current working string
                res += c
        
        return res