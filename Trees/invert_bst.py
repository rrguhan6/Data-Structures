from binary_search_tree import bst


class BST(bst):
    def invert(self, cur=None, _root=True):
        if(cur is None):
            if(self.root and _root == True):
                cur = self.root
                _root = False
            else:
                return None

        cur.left, cur.right = self.invert(
            cur.right, _root), self.invert(cur.left, _root)
        return cur


tree = BST()

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
print()
tree.invert()

tree.bfs()
