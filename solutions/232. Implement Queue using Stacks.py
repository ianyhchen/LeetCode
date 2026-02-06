class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek() # Ensure output stack has the current front
        return self.output.pop()
        

    def peek(self) -> int:
        if not self.output: #Transfer elements if output stack is empty
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]        

    def empty(self) -> bool:
        return not self.input and not self.output
'''
每個元素依照順序進出了stack兩次, LIFO 再 LIFO, 等價於 FIFO

Complexity Analysis
Push: Each push operation is O(1).
Pop and Peek: The cost of transferring elements from input to output is O(n) but happens only when output is empty. Therefore, the amortized cost is O(1) per operation.
Empty: This operation is O(1).
Space Complexity: O(n) to store elements in the two stacks.
'''        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()