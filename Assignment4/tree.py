import numpy as np
class Tree:
    """Abstract base class representing a tree structure."""
    
    #--------------------nested Position class------------------------------
    class Position:
        """An abstraction representing the location of a single element."""
        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')
            
        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        
        def __ne__(self, other):
            """Return True if other does not represent the smae location"""
            raise NotImplementedError('must be implemented by subclass')
            
    #--------abstract methods that concrete subclass must support--------------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')
        
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')
        
    def children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')
        
    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    #--------concrete methods implemented in this class--------------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
    
    def depth(self, p):
        """Return the number of levels seperating Position p from the root."""
        if self._is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height(self, p):     # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))
    
    def height(self, p = None):
        """Return the height of the subtree rooted at Position p
        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height(p) # start _height recursion
    
class GeneralTree(Tree):
    """Abstract base class representing a general tree structure"""
    # --------------------- additional abstract methods ---------------------
    def c_list(self, p):
        """Return a list containing p's children.
        
        Return None if p does not have a child
        """
        raise NotImplementedError('must be implemented by subclass')
        
    def sibling(self, p):
        """Return Positions representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None     # root has no sibling
        elif len(parent.c_list) == 1: # p is the only child of its parent
            return None     # p has no sibling
        else:
            for s in parent.c_list:
                if s != p:
                    yield s
                        
class LinkedTree(GeneralTree):
    class _Node:    # Lightweight, nonpublic clss for stroing a node.
        __slots__ = '_element', '_parent', '_c_list'
        def __init__(self, element, parent = None):
            self._element = element
            self._parent = parent
            self._c_list = []
            
    class Position(GeneralTree.Position):
        """An abstraction representing the location of a single element."""
        
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
            
        def element(self):
            """Return the element stored at this Position"""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
            
    def _validate(self, p):
            """Return associate node, if position is valide."""
            if not isinstance(p, self.Position):
                raise TypeError('p must be proper Position type')
            if p._container is not self:
                raise ValueError('p does not belong to this container')
            if p._node._parent is p._node: # convention for depreciated nodes
                raise ValueError('p is no longer valid')
            return p._node
            
    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
            
    #-------------------------- tree constructor --------------------------
    def __init__(self):
        """Create an initially empty tree."""
        self._root = None
        self._size = 0
        
    #-------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._right)
    
    def visit_child(self, p, n):
        """Return the Position of p's nth child (or None if no child)."""
        node = self._validate(p)
        return self._make_position(node._c_list[n])
    
    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        return len(node._c_list)
    
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        
        Raise ValueError if tree nonempty.
        """
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_child(self, p, e):
        """Create a new child for Position p, storing element e.
        
        Return the Position of new node.
        Raise ValueError if Position p is invalide or p already has a left child.
        """
        node = self._validate(p)
        self._size += 1
        node._c_list.append(self._Node(e, node))
        return self._make_position(node._c_list[-1])
    
#(a) Build the game tree
t = LinkedTree()    # Establish the empty tree
# add the root
t._add_root(np.asarray([None, None, None, None, None, None, None, None, None]))


def build_game(r):
    # tree root
    e = r.element() # root element
    if np.all((e != None)):
        if (e[0] == e[1] == e[2]) or (e[3] == e[4] == e[5]) or (e[6] == e[7] == e[8]) \
        or (e[0] == e[3] == e[6]) or (e[1] == e[4] == e[7]) or (e[2] == e[5] == e[8]) \
        or (e[0] == e[4] == e[8]) or (e[2] == e[4] == e[6]): # cross win
            return
    else:
        turn = 'X'
        if np.count_nonzero(e == 'X') > np.count_nonzero(e == 'O'):
            turn = 'O'
        for i in range(len(e)):
            if e[i] == None:
                add_e = np.copy(e)
                add_e[i] = turn
                t._add_child(r, add_e)
        for c in range(t.num_children(r)):
            build_game(t.visit_child(r, c))

build_game(t.root())

#def add_children(position, )
''' x = t.root()
t._add_child(x, ['X', None, None], [None, None, None], [None, None, None])
t.visit_child(x,0).element()
'''