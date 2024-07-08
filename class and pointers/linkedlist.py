class LInkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def append(self, value):
        current = self
        while current.next:
            current = current.next
        current.next = LInkedList(value)
    
    def pop(self):
        current = self
        while current.next.next:
            current = current.next
        current.next = None