class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

s = Stack()
s.push("H")
s.push("o")
s.push("l")
s.push("a")
s.push("!")
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())