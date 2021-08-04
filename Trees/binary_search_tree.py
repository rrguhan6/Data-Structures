
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

    # breadth first search - horizontal
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

    # depth first search - vertical
    def preorder(self, cur=None, temp = []):
        if(cur is None):
            if(self.root):
                cur = self.root
            else:
                return

        print(cur.data, end="  ")
        sol = []
        if(cur.left):
            _temp = [*temp, cur.left.data]
            sol = sol.append(self.preorder(cur.left , _temp , sol))
        if(cur.right):
            _temp = [*temp , cur.right.data]
            sol = sol.append(self.preorder(cur.right, _temp , sol))
        if(cur.left == None and cur.right == None):
            sol.append(temp)
            print(sol)
            return sol


    def postorder(self, cur=None):
        if(cur is None):
            if(self.root):
                cur = self.root
            else:
                return

        if(cur.left):
            self.postorder(cur.left)
        if(cur.right):
            self.postorder(cur.right)

        print(cur.data, end=" ")

    def inorder(self, cur=None):
        if(cur is None):
            if(self.root):
                cur = self.root
            else:
                return

        if(cur.left):
            self.inorder(cur.left)

        print(cur.data, end=" ")

        if(cur.right):
            self.inorder(cur.right)

    def search(self,  search_data, cur=None):
        if(cur is None):
            if(self.root is not None):
                cur = self.root
            else:
                return False
        print(cur.data)
        if(cur.data == search_data):
            return True
        else:
            if(cur.data < search_data):
                if(cur.right):
                    return self.search(search_data, cur.right)
                else:
                    return False
            else:
                if(cur.left):
                    return self.search(search_data, cur.left)

    def delete(self, delete_value):
        return self._delete(self.root, delete_value)

    def _leftmost(self, cur):
        current = cur

        while(current.left is not None):
            current = current.left

        return current

    def _delete(self, cur, key):

        if cur is None:
            return cur

        if key < cur.data:
            cur.left = self._delete(cur.left, key)

        elif(key > cur.data):
            cur.right = self._delete(cur.right, key)

        else:
            if cur.left is None:
                temp = cur.right
                cur = None
                return temp

            elif cur.right is None:
                temp = cur.left
                cur = None
                return temp

            temp = self._leftmost(cur.right)

            cur.data = temp.data

            cur.right = self._delete(cur.right, temp.data)

        return cur


"""
                    10
                 /      \
               6         15
              / \       /   \
            4     9   12      24
                 /          /    \
                7         20      30
                         /
                       18
"""

tree = bst()

tree.insert(10)
tree.insert(6)
tree.insert(4)
tree.insert(9)
# tree.insert(7)
# tree.insert(15)
# tree.insert(12)
# tree.insert(24)
# tree.insert(20)
# tree.insert(18)
# tree.insert(30)
#
#
tree.preorder()
# print()

# tree.delete(12)
#
# tree.bfs()
# print()
tree.preorder()