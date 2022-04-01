class BST:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val
    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BST(val)
            return
        if self.right:
            self.right.insert(val)
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
    def exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)
        if self.right == None:
            return False
        return self.right.exists(val)
    def size(self):
        size = 0
        if self != None:
            size += 1
            if self._leftchild != None:
                size += 1 + self._leftchild.size()
            if self._rightchild != None:
                size += 1 + self._rightchild.size()
        return size