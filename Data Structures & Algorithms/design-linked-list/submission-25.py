class MyLinkedList:

    def __init__(self, val=0, next=None, prev=None, head=None, tail=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.head = head
        self.tail = tail

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        new = MyLinkedList(val=val)
        if self.head:
            self.head.prev = new
            new.next = self.head
        else:
            self.tail = new
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = MyLinkedList(val=val)
        if self.tail:
            self.tail.next = new
            new.prev = self.tail
        else:
            self.head = new
        self.tail = new

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        if i < index:
            return
        if curr is None:
            self.addAtTail(val)
            return
        if curr is self.head:
            self.addAtHead(val)
            return
        
        new = MyLinkedList(val=val)
        new.prev = curr.prev
        new.next = curr
        curr.prev.next = new
        curr.prev = new
            
    def deleteAtIndex(self, index: int) -> None:
        if self.head and self.tail:
            curr = self.head
            if self.head is self.tail and index == 0:
                self.next = None
                self.head = None
            elif index == 0:
                self.head = curr.next
                curr.next.prev = None
            else:
                i = 0
                while curr:
                    if i == index:
                        if curr is self.tail:
                            self.tail = curr.prev
                            curr.prev.next = None
                        else:
                            curr.next.prev = curr.prev
                            curr.prev.next = curr.next
                        break
                    curr = curr.next
                    i += 1
                        
            



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)