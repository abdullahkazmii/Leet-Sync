class MyQueue:
    def __init__(self):
        self.stack_in = deque()  
        self.stack_out = deque() 

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._transfer_if_needed()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._transfer_if_needed()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
    
    def _transfer_if_needed(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()