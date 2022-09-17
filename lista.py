from hashlib import new
from node import DbNode


class SList:
    def __init__(self):
        self.head = None
        self.tail=None

    def add_to_front(self, val):
        new_node = DbNode(val)
        if self.head!=None:
            self.head.back=new_node
            new_node.next = self.head
        else:
            self.tail=new_node
        self.head = new_node
        
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        new_node = DbNode(val)
        if self.tail!=None:
            self.tail.next=new_node
            new_node.back = self.tail
        else:
            self.head=new_node
        self.tail = new_node
        return self
        

    def print_values_reverse(self):
        runner = self.tail
        while (runner != None):
            print(runner.value)
            runner = runner.back
        return self