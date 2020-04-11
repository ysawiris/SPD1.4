"""
Class: SPD 1.4 
Assignment: Coding Syntax 
"""

import Linked_List from "LinkedList.py"

class Stack:
    def _init_():
        this.List = new Linked_List();

    def push(newItem) :
        "Insert the given item on the top of this stack"
        // prepend given item before head node 
        this.List.prepend(newItem , index = 0);

    
    def peek() :
        "Return the item on the top of this stack"
        if ( this.List.head !== none ) {
            return(this.List.head.data[ 0 ]);
        }else{ return none; }

    def pop() :
        "Remove and return the item on the top of this stack"
        topItem=this.peak();
        this.List.delete(topItem);
        return(topItem);