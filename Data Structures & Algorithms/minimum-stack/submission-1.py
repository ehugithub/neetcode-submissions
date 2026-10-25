class MinStack:

    def __init__(self):
        self.lows = []
        self.stack = []
        self.lowest = float('inf')
        

    def push(self, val: int) -> None:
        self.lowest = min(self.lowest, val)
        self.stack.append(val)
        self.lows.append(self.lowest)
        

    def pop(self) -> None:
        self.stack.pop()
        self.lows.pop()
        self.lowest = float('inf') if not self.lows else self.lows[-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.lowest
