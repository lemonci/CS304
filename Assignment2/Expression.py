'''
The expression class can deal with operators +-*/ and numerical/algebrical operands, it does not have syntax checking functions.
The user should leave spaces around operands, operators and parenthesis.
To facilitate a two-way conversion, the converted expression also have spaces between operands, operators and parenthesis.
'''

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Expression():
    # use the ArrayStack class from lecture 6 to perform conversions and evaluations.
    # stack class should be a private field of the Expression class.
    _infix = ''
    _postfix = ''
    def __init__(self, input, direction):
        if (direction == '0'):
            self._infix = input
            self._postfix = self.in_to_post()
        elif (direction == '1'):
            self._postfix = input
            self._infix = self.post_to_in()
    
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

    def in_to_post(self):
        _in = self._infix.split()
        output = '' 
        S = self._ArrayStack()
        S.push('(')         # Push “(“ onto Stack
        _in.append(')')     # and add “)” to the end of input.
        for elem in _in:    # Scan the infix expression from left to right
            if elem == '(':     # If a left parenthesis is encountered,
                S.push(elem)    # push it onto Stack.)
            elif elem == ')':   # If a right parenthesis is encountered ,then:  
                while S.top() != '(':
                    output += ' '
                    output += S.pop()   # pop the stack and add it to output until a ‘(‘ is encountered
                S.pop()      # remove the left parenthesis
            elif elem not in '+-*/':    # If an operand is encountered,
                output += ' '
                output += elem          # add it to output
            else:   #If an operator is encountered         
                if elem in '+-':        # and add to output each operator
                    while S.top() != '(':  # (on the top of Stack) which has the same precedence as or higher precedence than operator.)
                        output += ' '
                        output += S.pop()   # Repeatedly pop from Stack
                    S.push(elem)        # Add operator to Stack
                else:
                    while S.top() not in '(+-':
                        output += ' '
                        output += S.pop()
                    S.push(elem)        # Add operator to Stack
        return output
             
    def post_to_in(self):
        _post = self._postfix.split()
        S2 = self._ArrayStack()
        for elem in _post:
            if elem in '+-*/': # suppose operator
                a = S2.pop()
                b = S2.pop()
                temp = '( ' + b + ' ' + elem + ' ' + a + ' )'
                S2.push(temp)
            else:   # suppose operand
                S2.push(elem)
                
        return S2.pop()[2:-2]
        
    def evaluate(self):
        if self._infix == '':
            self._infix = self.post_to_in()
        try:
            return eval(self._infix)
        except:
            return "the expression cannot be evaluated"
#Testing        
if __name__ == '__main__':
    print('Input an expression, leave spaces around operands, operators and parenthesis:')
    expr = input()
    # test case1: 6 * ( 5 + ( 2 + 3 ) * 8 + 3 )
    # test case2: a b c * + d e * f + g * +
    print('Input the direction: 0 for infix to postfix, 1 for postfix to infix')
    drct = input()
    test = Expression(expr, drct)
    print('postfix: ', test.in_to_post())
    print('infix: ', test.post_to_in())
    print('evaluation: ', test.evaluate())