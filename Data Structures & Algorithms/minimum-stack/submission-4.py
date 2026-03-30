class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
            return
        minVal = min(val, self.minStack[-1])
        self.minStack.append(minVal)
        
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
        


#intuition is we want to keep track of the min element each time an element is added to the stack
#push to a minstack each time we push to regular stack and also remove