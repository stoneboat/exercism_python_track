class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message


class Node:
    def __init__(self, value):
        self._value = value 
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        
        if values is None:
            self._head = None
        else:
            self._head = None

            for value in values:
                node = Node(value)
                if self._head is None:
                    self._head = node
                else:
                    node._next = self._head 
                    self._head = node

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current.value()
            current = current.next()

    def __len__(self):
        current = self._head 

        count = 0
        while current is not None:
            count += 1 
            current = current.next()
        
        return count

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        else:
            return self._head


    def push(self, value):
        node = Node(value)
        if self._head is None:
            self._head = node
        else:
            node._next = self._head 
            self._head = node

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        else:
            value = self._head.value()
            self._head = self._head.next()

        return value

    def reversed(self): 
        return LinkedList(list(self))
