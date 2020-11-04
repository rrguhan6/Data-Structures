
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
    def preorder(self, cur=None):
        if(cur is None):
            if(self.root):
                cur = self.root
            else:
                return

        print(cur.data, end="  ")

        if(cur.left):
            self.preorder(cur.left)
        if(cur.right):
            self.preorder(cur.right)

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

    # def delete(self, delete_data, cur=None):
    #     if(cur is None):
    #         if(self.root is not None):
    #             cur = self.root
    #         else:
    #             return False

    #     if(cur.data == delete_data):
    #         if(cur.right):
    #             pass
    #         else:
    #             if(cur.left):
    #                 pass
    #             else:

    #     else:
    #         if(cur.data < delete_data):
    #             if(cur.left):
    #                 return self.delete(delete_data, cur.left)
    #             else:
    #                 return False
    #         else:
    #             if(cur.right):
    #                 return self.delete(delete_data, cur.right)
    #             else:
    #                 return False


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
tree.insert(7)
tree.insert(15)
tree.insert(12)
tree.insert(24)
tree.insert(20)
tree.insert(18)
tree.insert(30)


# tree.inorder()

# print(tree.search(search_data=20))
