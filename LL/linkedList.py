class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
            self.length += 1
        return True
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
        
    def insert(self, index, value):
        pass
    
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            pre.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value
    
    def popfirst(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


my_linked_list = LinkedList(1)

#print(my_linked_list.head.value) # 4

#my_linked_list.print_list() # 4

my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.print_list() # 4, 3

#print(my_linked_list.pop()) 
#print(my_linked_list.pop())
#print(my_linked_list.pop())

my_linked_list.prepend(5)
my_linked_list.print_list()

print(my_linked_list.get(0).value)