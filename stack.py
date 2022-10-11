
class NullElementException(Exception): pass

class EmptyStackException(Exception): pass


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def empty(self):
        return self.items == []

    def push(self, item):
        if not item : raise NullElementException
        self.items.append(item)

    def pop(self):
        if self.empty(): raise EmptyStackException
        return self.items.pop()

    def peek(self):
        if self.empty(): raise EmptyStackException
        return self.items[-1]