class Node:
    """Binary Tree"""
    def __init__(self, key_=None, val_=None) -> None:
        self.left = None
        self.right = None
        self.key = key_
        self.val = val_

    def insert(self, key_, val_):
        if self.key:
            if key_ < self.key:
                if self.left is None:
                    self.left = Node(key_, val_)   
                else:
                    self.left.insert(key_, val_)
            elif key_ > self.key:
                if self.right is None:
                    self.right = Node(key_, val_)
                else:
                    self.right.insert(key_, val_)
            else:
                self.key = key_
                self.val = val_    
        else:
            self.key = key_
            self.val = val_

        return (key_, val_)    
    
    def get(self, key_):
        if key_ < self.key:
            if self.left:
                self.left.get(key_)
            else:
                return (key_, None)
        elif key_ > self.key:
            if self.right:
                self.right.get(key_)
            else:
                return (key_, None)
        else:
            return (key_, self.val)
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print((self.key, self.val))
        if self.right:
            self.right.print_tree()
        

class TreeMap:
    """Tree Map in Binary Tree"""
    def __init__(self) -> None:
        self.map_tree = Node()
     
    def put_val(self, key_, val_):
        if key_:
            return self.map_tree.insert(key_, val_)
        return None

    def get_val(self, key_):
        return self.map_tree.get(key_)

    def print_tree(self):
        self.map_tree.print_tree()


tmap = TreeMap()
tmap.print_tree()
tmap.put_val(1, 'pmp')
tmap.print_tree()
tmap.put_val(1, 'pamp')
tmap.put_val(2, 'ada')
tmap.put_val(3, 'erde')
tmap.put_val(4, 'bfff')
tmap.put_val(5, 'ereee')
tmap.put_val(6, 'oto')
tmap.print_tree()
print('---')
print(tmap.get_val(1))
print('----')

