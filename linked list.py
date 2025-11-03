class Node:
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node

    def set_next(self, node):
        self._next_node=node
        pass

    def get_next(self):
        return self._next_node
        pass

    def get_data(self):
        return self._data
        pass

class LinkedList:
    """
    A stack using a singly linked list to create a stack.
    """
    def __init__(self):
        self._head_node = None
        self._size = 0

    def __len__(self):
        return self._size
        """ Allows the use of len(stack) to find the number of elements in the stack """
        pass

    def push(self, data):
        self._head_node=Node(data,self._head_node)
        self._size+=1
        pass

    def pop(self):
        if self._size==0:
            print("the queue has no items in it and so cannot have an item removed from it")
        else:
            temp=self._head_node.get_data()
            self._head_node=self._head_node.get_next()
            self._size-=1
            return temp
        pass

    def peek(self):
        return self._head_node
        pass
    
    def is_empty(self):
        return self._size == 0
    
    def append(self,data):
        self.push(data)

    
    def __str__(self):
        string=""
        next=self._head_node
        while next!=None:
            string+=str(next.get_data())
            next=next.get_next()


        """ Defines what should be displayed when the user prints a linked list object. """
        return string

if __name__ == "__main__":
    my_stack = LinkedList()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.append(4)

    print(my_stack, len(my_stack))

    while not my_stack.is_empty():
        print(my_stack.pop())
print(my_stack.pop())