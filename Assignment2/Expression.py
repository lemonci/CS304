class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Expression():
    # use the ArrayStack class from lecture 6 to perform conversions and evaluations.
    # stack class should be a private field of the Expression class.
    
    class _ArrayStack:
        """LIFO Stack implementation using a Python list as underlying storage."""
        def __init__(self):
            """Create an empty stack."""
            self._data = [] # nonpublic list instance
        def __len__(self):
            """Return the number of elements in the stack."""
            return len(self._data)
        def is_empty(self):
            return len(self._data) == 0
        
        def push(self, e):
            """Add element e to the top of the stack."""
            self._data.append(e)        # new item stored at end of list
            
        def top(self):
            """Return (but do not remove) the element at the top of the stack.
            
            Raise Empty exception if the stack is empty.
            """
            if self.is_empty():
                raise Empty('Stack is empty')
            return self._data[-1]       # the last item in the list
        
        def pop(self):
            """Remove and return the element from the top of the stack (i.e., LIFO).
            
            Raise Empty exception if the stack is empty.
            """
            if self.is_empty():
                raise Empty('Stack is empty')
            return self._data.pop()         # remove last item from list
        
#        def full_stack(self):
#            return self._data

    def in_to_post():
        print('Input an infix expression, leave spaces around operands, operators and parenthesis: ')
        _in = input().split()
        output = '' 
        S = Expression._ArrayStack()
        S.push('(')         # Push “(“ onto Stack
        _in.append(')')     # and add “)” to the end of input.
        for elem in _in:    # Scan the infix expression from left to right
            if elem == '(':     # If a left parenthesis is encountered,
                S.push(elem)    # push it onto Stack.)
            elif elem == ')':   # If a right parenthesis is encountered ,then:  
                while S.top() != '(':
                    output += S.pop()   # pop the stack and add it to output until a ‘(‘ is encountered
                S.pop()      # remove the left parenthesis
            elif elem not in '+-*/':    # If an operand is encountered,
                output += elem          # add it to output
            else:   #If an operator is encountered         
                if elem in '+-':        # and add to output each operator
                    while S.top() != '(':  # (on the top of Stack) which has the same precedence as or higher precedence than operator.)
                        output += S.pop()   # Repeatedly pop from Stack
                    S.push(elem)        # Add operator to Stack
                else:
                    while S.top() not in '(+-':
                        output += S.pop()
                    S.push(elem)        # Add operator to Stack
        return output
                
    def post_to_in():
        