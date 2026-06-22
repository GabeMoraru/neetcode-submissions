class ListNode:
    
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(val=homepage)

    def visit(self, url: str) -> None:
        new = ListNode(val=url, prev=self.curr)
        self.curr.next = new
        self.curr = new

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.prev:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next and i < steps:
            self.curr = self.curr.next
            i += 1
        return self.curr.val

        # 1 - 2 - 3 - 4


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)