
class node:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if(self.root == None):
            self.root = node(data)
            return True

        return self.recur_insert(self.root, data)

    def recur_insert(self, cur, data):

        if(cur.data == data):
            return False
        elif(data < cur.data):
            if(cur.left):
                return self.recur_insert(cur.left, data)
            else:
                cur.left = node(data)
                return True
        else:
            if(cur.right):
                return self.recur_insert(cur.right, data)
            else:
                cur.right = node(data)
                return True

    # breadth first search
    def bfs(self):
        _q = []
        _q.append(self.root)

        while(_q):
            cur = _q.pop(0)
            print(cur.data, end=" ")

            if(cur.left):
                _q.append(cur.left)
            if(cur.right):
                _q.append(cur.right)


tree = bst()

tree.insert(10)
tree.insert(6)
tree.insert(4)
tree.insert(9)
tree.insert(7)
tree.insert(15)
tree.insert(12)
tree.insert(24)
tree.insert(20)
tree.insert(18)
tree.insert(30)


tree.bfs()
