class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = [float('inf')]

    def push(self, val: int) -> None:
        if len(self.mini) == 0:
            self.mini.append(val)
        else:
            self.mini.append(min(self.mini[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.mini = self.mini[:-1]
        self.stack = self.stack[:-1]


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
