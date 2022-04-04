import random
from random import shuffle 
#1) BST (binary search tree)
class BST:
    def __init__(self, pair = None):
        self.left = None
        self.right = None
        self.pair = pair
        
    def insert(self, pair):
        if not self.pair:
            self.pair = pair
            return
        if self.pair[0] == pair[0]:
            return
        if pair[0] < self.pair[0]:
            if self.left:
                self.left.insert(pair)
                return
            self.left = BST(pair)
            return
        if self.right:
            self.right.insert(pair)
            return
        self.right = BST(pair)
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.pair[0]
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.pair[0]
    def __delitem__(self, key):
        if self == None:
            return self
        if key < self.pair[0]:
            self.left = self.left.__delitem__(key)
            return self
        if key > self.pair[0]:
            self.right = self.right.__delitem__(key)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node:
            min_larger_node = min_larger_node.left
        self.pair = min_larger_node.pair
        self.right = self.right.__delitem__(min_larger_node.key)
        return self
    def exists(self, key):
        if key == self.pair[0]:
            return True
        if key < self.pair[0]:
            if self.left == None:
                return False
            return self.left.exists(key)
        if self.right == None:
            return False
        return self.right.exists(key)
    def __len__(self):
        size = 0
        if self.pair != None:
            size += 1
            if self.left != None:
                size += self.left.__len__()
            if self.right != None:
                size += self.right.__len__()
        return size
    
    def __getitem__(self, key):
        if key == self.pair[0]:
            return self.pair[1]
        if key < self.pair[0]:
            if self.left == None:
                raise KeyError("%s is not in the tree." % key)
            return self.left.__getitem__(key)
        if self.right == None:
            raise KeyError("%s is not in the tree." % key)
        return self.right.__getitem__(key)
        
    def __setitem__(self, key, val):
        pair_n = (key, val)
        if key == self.pair[0]:
            self.pair = pair_n
            return
        if key < self.pair[0]:
            if self.left == None:
                raise KeyError("%s is not in the tree." % key)
            self.left.__setitem__(key, val)
        if self.right == None:
            raise KeyError("%s is not in the tree." % key)
        self.right.__setitem__(key, val)


#4) skip list  
class SkipList(object):
    class Node(object):
        # Class to implement node
        def __init__(self, pair, level):
            self.pair = pair
            # list to hold references to node of different level 
            self.forward = [None]*(level+1)

    def __init__(self, max_lvl, P):
        # Maximum level for this skip list
        self.MAXLVL = max_lvl
  
        # P is the fraction of the nodes with level 
        # i references also having level i+1 references
        self.P = P
  
        # create header node and initialize key to -1
        self.header = self.createNode(self.MAXLVL, -1)
  
        # current level of skip list
        self.level = 0
      
    # create  new node
    def createNode(self, lvl, pair):
        n = self.Node(pair, lvl)
        return n
      
    # create random level for node
    def randomLevel(self):
        lvl = 0
        while random.random()<self.P and \
              lvl<self.MAXLVL:lvl += 1
        return lvl
  
    # insert given key in skip list
    def insertElement(self, pair):
        # create update array and initialize it
        update = [None]*(self.MAXLVL+1)
        current = self.header
  
        '''
        start from highest level of skip list
        move the current reference forward while key 
        is greater than key of node next to current
        Otherwise inserted current in update and 
        move one level down and continue search
        '''
        for i in range(self.level, -1, -1):
            while current.forward[i] and \
                  current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
  
        ''' 
        reached level 0 and forward reference to 
        right, which is desired position to 
        insert key.
        ''' 
        current = current.forward[0]
  
        '''
        if current is NULL that means we have reached
           to end of the level or current's key is not equal
           to key to insert that means we have to insert
           node between update[0] and current node
       '''
        if current == None or current.key != key:
            # Generate a random level for node
            rlevel = self.randomLevel()
  
            '''
            If random level is greater than list's current
            level (node with highest level inserted in 
            list so far), initialize update value with reference
            to header for further use
            '''
            if rlevel > self.level:
                for i in range(self.level+1, rlevel+1):
                    update[i] = self.header
                self.level = rlevel
  
            # create new node with random level generated
            n = self.createNode(rlevel, key)
  
            # insert node by rearranging references 
            for i in range(rlevel+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n
  
            print("Successfully inserted key {}".format(key))
  
    # Display skip list level wise
    def displayList(self):
        print("\n*****Skip List******")
        head = self.header
        for lvl in range(self.level+1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while(node != None):
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")
    
LEN = 10
keys = list(range(LEN))
shuffle(keys)


dic = []
for key in keys:
    dic.append((key, random.random()))

# ===========================insertion for BST==============================
# tree = BST()
# for item in dic:
#     tree.insert(item)
# =============================================================================
