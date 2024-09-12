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
        pass
        
    def insert(self, index, value):
        pass
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)

#print(my_linked_list.head.value) # 4

#my_linked_list.print_list() # 4

my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list() # 4, 3