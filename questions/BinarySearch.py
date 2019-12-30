class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        insert new node with data

        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            print("cannot insert child Node with same value")

    def lookup(self, data, parent=None):
        """
        lookup node containing data

        @param data node data object to loop up
        @param parent node's parent
        @return node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        """
        returns the number of children
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        node, parent = root.lookup(data)
        if node == None:
            return

        children_count = node.children_count()
        if children_count == 0:
            #0 children
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            del node
        elif children_count == 0:
            #1 chile
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
            del node
        else:
            #2 children
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            #replace node dta by it's successor data
            node.data = successor.data
            #fix successor's parent's child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

root.print_tree()