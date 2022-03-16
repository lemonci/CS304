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
        __slots__ = 'element', '_parent', 'c_list'