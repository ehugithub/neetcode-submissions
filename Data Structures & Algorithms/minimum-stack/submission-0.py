class MinStack:

    def __init__(self):
        # keep a stack of indexes of previous mins: if i pop a min, i pop the corresp ind as well
        # since list lookup is constant
        self.st = []
        self.sz = 0
        self.inds = [] 

    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.inds or value < self.getMin():
            self.inds.append(self.sz)
        self.sz += 1 

    def pop(self) -> None:
        val = self.st.pop()
        if self.inds[-1] == self.sz - 1:
            self.inds.pop()
        self.sz -= 1

    def top(self) -> int:
        return self.st[-1] 

    def getMin(self) -> int:
        return self.st[self.inds[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()