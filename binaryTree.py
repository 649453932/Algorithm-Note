class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历
def preorder1(root):
    if root is None:
        return
    print(root.val)
    preorder1(root.left)
    preorder1(root.right)


def preorder2(root):
    tmp = []
    while tmp or root:
        while root:
            print(root.val)
            tmp.append(root.right)
            root = root.left
        root = tmp.pop()


# 中序遍历:
def inorder1(root):
    if root is None:
        return
    preorder1(root.left)
    print(root.val)
    preorder1(root.right)


def inorder2(root):
    tmp = []
    while tmp or root:
        while root:
            tmp.append(root)
            root = root.left
        root = tmp.pop()
        print(root.val)
        root = root.right


# 后序遍历:
def postorder1(root):
    if root is None:
        return
    preorder1(root.left)
    preorder1(root.right)
    print(root.val)


# 把前序遍历：前左右 改为 前右左，这种前序遍历逆序就是后序遍历了
def postorder2(root):
    res = []
    tmp = []
    while tmp or root:
        while root:
            res.append(root.val)
            tmp.append(root.left)
            root = root.right
        root = tmp.pop()
    res = res[::-1]
    for data in res:
        print(res)
