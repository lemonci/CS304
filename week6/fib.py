def fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return (n,0)
    else:
        (a, b) = fibonacci(n-1)
        return (a+b, a)
    
    
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    grandparent = 0
    parent = 1
    for i in range(2,n+1):
        me = parent + grandparent
        grandparent = parent
        parent = me
    return me

def fib_sum(n):
    if n<= 1:
        return n
    else:
        return fib_sum(n-2) + fib_sum(n-1)