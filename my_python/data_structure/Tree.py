class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:

    @staticmethod
    def serialize(root: TreeNode) -> str:
        def helper(root):
            if not root:
                return 'null'
            return str(root.val) + ',' + helper(root.left) + ',' + helper(root.right)
        return helper(root)

    @staticmethod
    def deserialize(data: str) -> TreeNode:
        data = data.split(',')

        def helper(data):
            print(data)
            x = data.pop(0)
            if x == 'null':
                return None
            node = TreeNode(int(x))
            node.left = helper(data)
            node.right = helper(data)
            return node
        return helper(data)


class Tree:

    @staticmethod
    def traversal(root: TreeNode, way: str = 'seq') -> list:
        re, qu = [], [root]

        if not root:
            return re

        if way == 'seq':
            while len(qu):
                node = qu.pop(0)
                re.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
        else:
            def helper(root):
                if not root:
                    return
                if way == 'pre':
                    re.append(root.val)
                helper(root.left)
                if way == 'inf':
                    re.append(root.val)
                helper(root.right)
                if way == 'pos':
                    re.append(root.val)
            helper(root)

        return re

    @staticmethod
    def create(way: str = 'in', inf: list[int] = [], x: list[int] = []) -> TreeNode:
        if way == 'in':
            def helper() -> TreeNode:
                val = input('please enter the node value, # is null:')
                if val == '#':
                    return None
                node = TreeNode(int(val), helper(), helper())
                return node
            return helper()
        else:
            def helper(inf: list[int], x: list[int]) -> TreeNode:
                if not len(inf):
                    return None
                if way == 'xi':
                    i = inf.index(x[0])
                    node = TreeNode(inf[i], helper(
                        inf[:i], x[1:i+1]), helper(inf[i+1:], x[i+1:]))
                if way == 'ix':
                    i = inf.index(x[-1])
                    node = TreeNode(inf[i], helper(
                        inf[:i], x[:i]), helper(inf[i+1:], x[i:-1]))
                return node
            return helper(inf, x)

    @staticmethod
    def reverse(root: TreeNode) -> None:
        def helper(root):
            if root is not None:
                helper(root.left)
                helper(root.right)
                root.left, root.right = root.right, root.left
        helper(root)

    @staticmethod
    def get_height(root: TreeNode) -> int:
        def helper(root):
            return max(helper(root.left), helper(root.right)) + 1 if root is not None else 0
        return helper(root)

    @staticmethod
    def paths(root: TreeNode) -> list[str]:
        paths, path = [], ''

        def helper(root, path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += '->'
                helper(root.left, path)
                helper(root.right, path)
        helper(root, '')

        return paths


def run():

    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))

    print(Codec.serialize(root))

if __name__ == '__main__':

    run()