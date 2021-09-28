class newNode:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def fillMap(root, d, l, m):
    if root is None:
        return

    if d not in m:
        m[d] = [root.data, l]
    elif m[d][1] > l:
        m[d] = [root.data, l]
    fillMap(root.left, d - 1, l + 1, m)
    fillMap(root.right, d + 1, l + 1, m)


def topView(root):
    m = {}

    fillMap(root, 0, 0, m)
    for it in sorted(m.keys()):
        print(m[it][0], end=" ")


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
topView(root)
