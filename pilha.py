class Node:
    def __init__(self,data):
        self.data = data
        self.next = Node

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size +=1

    def pop(self):
        if self.size == 0:
            return 'Pilha Vazia'
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.data
    
    def peek(self):
        if self.size == 0:
            return 'Pilha Vazia'
        return self.top.data


    def empty(self):
        return self.size == 0

    
    def __repr__(self):
        if self.size == 0:
            return 'Pilha Vazia'
        
        s = ''
        p = self.top
        while(p):
            s += str(p.data) + '\n'
            p = p.next
        return s
    

pilha = Stack()
pilha.push(10)
pilha.push(25)
pilha.push(33)
print(pilha.__repr__())
print(pilha.size)

print(pilha.empty())

pilha.pop()


print(pilha.__repr__())
print(pilha.size)

