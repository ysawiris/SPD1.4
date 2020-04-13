"""
Class: SPD 1.4 
Assignment: Coding Syntax 
"""

from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, newItem):
        "Insert the given item on the top of this stack"
        #prepend given item before head node 
        self.list.prepend(newItem)

    def peek(self):
        "Return the item on the top of this stack"
        if self.list.head != None:
            return self.list.head.data[0]
        else:
            return None

    def pop(self) :
        "Remove and return the item on the top of this stack"
        topItem = self.peek()
        self.list.delete(topItem)
        
        return(topItem)