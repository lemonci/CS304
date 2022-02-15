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

    def in_to_post():
        print('Input an infix expression, leave spaces around operands, operators and parenthesis: ')
        _in = input().split()
        output = '' 
        S = _ArrayStack()
        S.push('(')         # Push “(“onto Stack
        _in.append(')')     # and add “)” to the end of input.
        for elem in _in:    # Scan the infix expression from left to right
            if elem == '(':     # If a left parenthesis is encountered,
                S.push(elem)    # push it onto Stack.
            elif elem == ')':   # If a right parenthesis is encountered ,then:
                temp = S.pop()  # pop the stack and output it until a ‘(‘ is encountered
                while temp != '(':  # and discard both the parenthesis.
                    output += temp
                    temp = S.pop()
            elif elem not in '+-*/':    # If an operand is encountered, 
                output += elem          # add it to output
            else:   #If an operator is encountered
                temp = S.pop()          # Repeatedly pop from Stack 
                if elem in '+-':        # and add to output each operator 
                    while temp != '(':  # (on the top of Stack) which has the same precedence as or 
                        output += temp  # higher precedence than operator.
                        temp = S.pop()
                    S.push(temp)
                    S.push(elem)        # Add operator to Stack
                else:
                    while temp not in '(/*':
                        output += temp
                        temp = S.pop()
                    S.push(temp)
                    S.push(elem)        # Add operator to Stack
        return output
                
        