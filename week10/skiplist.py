"""
Skip list:
consider of a series of lists: {S0, S1, ..., Sh} storing a subset of items M, sorted by increasing key, plus sentinels -inf, +inf.

Search for 44:
"""
S.find(44)
item = S[44]
#Start from left heightest.
SkipSearch(k):
    p = start
    while below(p) != None do
        p = below(p)
        while k >= Key(next(p))
            p = next(p)
            
    return p
    
SkipInsert(k, v):
    p = SkipSearch(k) # bottom level item with largest key <= k
    q = None
    i = -1
    if (Key(p)) == k) => override value with v
    else create new node after p
    repeat:
        i = i + 1
        if i >= h then
            h = h + 1
            t = next(s) # s is -inf
            s = insertAfterAbove(None, s, (-inf, None))
            insertAfterAbove(s, t, (+inf, None))
            
    while above p is None do
        p = prev(p)
    p = above(p)
    q = insertAfterAbove(p, q, (K, v))
    until coinFlip() == tails
    n = n + 1
    return q