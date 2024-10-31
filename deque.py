class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.preview = None

class Deck:
    def __init__(self):
        self.left = None
        self.right = None
        self._size = 0

    def push_left(self,elem):
        node = Node(elem)
        if self.left is None:
            self.left = node
            self.right = node
        else:
            self.left.preview = node
            node.next = self.left
            self.left = node
        self._size +=1

    def push_right(self,elem):
        node = Node(elem)
        if self.right is None:
            self.right = node
            self.left = node
        else:
            node.preview = self.right
            self.right.next = node
            self.right = node
        self._size +=1

    def pop_left(self):
        if self.empty():
            return 'Deque Vazio!'
        
        elem = self.left.data
        if self.left == self.right:  
            self.left = None
            self.right = None
        else:
            self.left = self.left.next
            self.left.preview = None
        self._size -= 1
        return elem

        
    def pop_right(self):
        if self.empty():
            return 'Deque Vazio!'
        
        elem = self.right.data
        if self.left == self.right:  
            self.left = None
            self.right = None
        else:
            self.right = self.right.preview
            self.right.next = None
        self._size -= 1
        return elem
        
    def peek_right(self):
        if self.empty():
            return 'Deque Vazio!'
        return self.right.data
    
    def peek_left(self):
        if self.empty():
            return 'Deque Vazio!'
        return self.left.data
        
    
    


    def __len__(self):
        return self._size
    
    def empty(self):
        return len(self) == 0
    
    def __repr__(self):
        if self.empty():
            return 'Deque Vazio!'
        
        p = self.left
        s = 'left << '
        while (p):
            s += str(p.data)
            p = p.next
            if p:
                s += ' | '
        s += ' >> right'
        return s
    
a = Deck()
a.push_left(5)
a.push_left(25)
a.push_right(57)
a.push_right(23)
print(a.__repr__())
print(f'Tamanho: {a.__len__()}')
print(f'Vazio: {a.empty()}')
print(f'Numero mais a esquerda: {a.peek_left()}')
print(f'Numero mais a direita: {a.peek_right()}')
a.pop_left()
a.pop_right()
print(a.__repr__())