class ArrayStack:
    """LIFO Stack implementation using a python list as underlying storage"""
    def __init__(self):
        """Create an empty stack"""
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        """Return true if stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()
    
a = [1, 2, 3]
s = ArrayStack()
for i in range(len(s)):
    s.push(a[i])
    
while not s.is_empty():
    a[i] = s.pop() #????
    
    
def is_matched(expr):
    """return true if all delimiters match"""
    lefty = '([{'
    righty = ')]}'
    s = ArraryStack[]
    for  c in expr:
        if c is in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop())
                return False
    return s.is_empty()