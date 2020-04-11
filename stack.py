import Linked_List from "Linkedkist.py"

class Stack:
    def __init__() :
        this.List = new Linked_List();
    
    def push(newItem) :
        "Insert the given item on the top of this stack"
        //prepend given item before head node
        this.List.prepend(newItem , index = 0);
    
    def peek() :
        "Return the item on the top of this stack"
        if ( this.List.head !== none ) {
            return(this.List.head.data[ 0 ]):
        }