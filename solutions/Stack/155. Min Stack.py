'''
Two Stack solution
一個主棧存資料，一個輔助棧存「對應當前狀態的最小值」。
'''
class MinStack:

    def __init__(self):
        # Primary stack to store all elements
        self.primary_stack = []
        # Store the minimum value for each state
        self.min_stack = []

    def push(self, val: int) -> None:
        self.primary_stack.append(val)

        # If min_stack is empty, current val is the min.
        # Otherwise, compare val with the current top of min_stack.
        if not self.min_stack: 
            self.min_stack.append(val)
        else:
            top = self.min_stack[-1]
            self.min_stack.append(min(top, val))         

    def pop(self) -> None:
        # slicing [:-1] will create a new list and copy all of the rest value,
        # which is O(n) time complexity
        if self.primary_stack:
            self.primary_stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        # Return the last element of the primary stack
        return self.primary_stack[-1]

    def getMin(self) -> int:
        # Return the last element of the min_stack, which is the current minimum
        return self.min_stack[-1]

'''
單棧存元組 (Pair/Tuple Approach)
在同一個棧中存入元組 (value, current_min)
'''
class MinStack:

    def __init__(self):       
        self.stack = []       

    def push(self, val: int) -> None:    
        if not self.stack: 
            pair = (val, val)
            self.stack.append(pair)
        else:
            pair = (val, min(val, self.getMin()))
            self.stack.append(pair)         

    def pop(self) -> None:
        # slicing [:-1] will create a new list and copy all of the rest value,
        # which is O(n) time complexity
        if self.stack:
            self.stack.pop()          
        
    def top(self) -> int:
        # Return the last element of the stack
        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        # Return the minimum value from last element of the stack
        _, min_val = self.stack[-1]
        return min_val
