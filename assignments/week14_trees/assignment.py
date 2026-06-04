from __future__ import annotations

"""Week 14 assignment starter for Trees."""

from dataclasses import dataclass

WEEK_NUMBER = 14
TOPIC = 'Trees'
FEATURE_NAME = 'Hierarchy Visualization Center'

LEARNING_OBJECTIVES = [
    "Implement binary search tree insertion.",
    "Traverse trees in multiple orders.",
    "Measure tree height.",
]


@dataclass
class TreeNode:
    """A single node in a binary search tree. Already implemented — do not modify."""
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


class BinarySearchTree:
    """A Binary Search Tree (BST).

    Rule: left child < parent < right child.
    """

    def __init__(self) -> None:
        """Initialize an empty tree with self.root = None."""
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        """Insert value into the BST.

        Examples:
            Inserting into an empty tree makes that value the root:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.root.value
                10

            A smaller value goes to the left of the root:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.insert(5)
                >>> bst.root.left.value
                5

            A larger value goes to the right of the root:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.insert(15)
                >>> bst.root.right.value
                15

            Duplicate values are ignored — the BST only stores unique values:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.insert(10)
                >>> bst.root.left is None and bst.root.right is None
                True

        Hints:
            Define a helper inside this method:
                def _insert(node, new_value):
                    if node is None: return TreeNode(new_value)
                    if new_value < node.value: node.left = _insert(node.left, new_value)
                    elif new_value > node.value: node.right = _insert(node.right, new_value)
                    return node
            Then call: self.root = _insert(self.root, value)
        """
        def _insert(node, new_value):
            if node is None:
                return TreeNode(new_value)
            if new_value < node.value:
                node.left = _insert(node.left, new_value)
            elif new_value > node.value:
                pass  # TODO: set node.right = _insert(node.right, new_value)
            return node
        self.root = _insert(self.root, value)

    def search(self, value: int) -> bool:
        """Return True if value exists in the tree, False otherwise.

        Examples:
            A value that was inserted is found:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.search(10)
                True

            A value that was never inserted is not found:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.search(99)
                False

            Searching an empty tree always returns False:
                >>> bst = BinarySearchTree()
                >>> bst.search(5)
                False

            A value inserted as a left child is found:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.insert(5)
                >>> bst.search(5)
                True

            A value inserted as a right child is found:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.insert(15)
                >>> bst.search(15)
                True

        Hints:
            current = self.root
            while current is not None:
                if current.value == value: return True
                elif value < current.value: current = current.left
                else: current = current.right
            return False
        """
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif value < current.value:
                current = None  # TODO: replace None — move to the left child
            else:
                current = None  # TODO: replace None — move to the right child
        return False

    def inorder(self) -> list[int]:
        """Return all values in ascending order (left, node, right).

        Examples:
            Three values inserted in random order; inorder returns them sorted:
                >>> bst = BinarySearchTree()
                >>> for v in [10, 5, 15]: bst.insert(v)
                >>> bst.inorder()
                [5, 10, 15]

            An empty tree returns an empty list:
                >>> bst = BinarySearchTree()
                >>> bst.inorder()
                []

            A single node returns a one-element list:
                >>> bst = BinarySearchTree()
                >>> bst.insert(42)
                >>> bst.inorder()
                [42]

            Inorder traversal always produces a sorted sequence for a valid BST:
                >>> bst = BinarySearchTree()
                >>> for v in [20, 10, 30, 5, 15]: bst.insert(v)
                >>> bst.inorder()
                [5, 10, 15, 20, 30]

        Hint:
            def _walk(node):
                if node is None: return []
                return _walk(node.left) + [node.value] + _walk(node.right)
            return _walk(self.root)
        """
        def _walk(node):
            if node is None:
                return []
            return None  # TODO: replace None — return _walk(node.left) + [node.value] + _walk(node.right)
        return _walk(self.root)

    def preorder(self) -> list[int]:
        """Return values in preorder (node, left, right).

        Hint:
            def _walk(node):
                if node is None: return []
                return [node.value] + _walk(node.left) + _walk(node.right)
            return _walk(self.root)
        """
        def _walk(node):
            if node is None:
                return []
            return None  # TODO: replace None — return [node.value] + _walk(node.left) + _walk(node.right)
        return _walk(self.root)

    def postorder(self) -> list[int]:
        """Return values in postorder (left, right, node).

        Hint:
            def _walk(node):
                if node is None: return []
                return _walk(node.left) + _walk(node.right) + [node.value]
            return _walk(self.root)
        """
        def _walk(node):
            if node is None:
                return []
            return None  # TODO: replace None — return _walk(node.left) + _walk(node.right) + [node.value]
        return _walk(self.root)

    def get_height(self) -> int:
        """Return the height of the tree. An empty tree has height 0.

        Examples:
            An empty tree has height 0:
                >>> bst = BinarySearchTree()
                >>> bst.get_height()
                0

            A single root node has height 1:
                >>> bst = BinarySearchTree()
                >>> bst.insert(10)
                >>> bst.get_height()
                1

            A tree with root, one left child, and one right child has height 2:
                >>> bst = BinarySearchTree()
                >>> for v in [10, 5, 15]: bst.insert(v)
                >>> bst.get_height()
                2

            A deeper tree with five nodes has height 3:
                >>> bst = BinarySearchTree()
                >>> for v in [10, 5, 15, 3, 7]: bst.insert(v)
                >>> bst.get_height()
                3

        Hint:
            def _height(node):
                if node is None: return 0
                return 1 + max(_height(node.left), _height(node.right))
            return _height(self.root)
        """
        def _height(node):
            if node is None:
                return 0
            return None  # TODO: replace None — return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)


def is_complete() -> bool:
    """Return completion status for this week's assignment starter."""
    return False


def get_unlocked_feature() -> str:
    """Return the dashboard feature unlocked by this week."""
    return FEATURE_NAME


def get_week_summary() -> dict[str, object]:
    """Return a dashboard-friendly summary for this week."""
    return {
        'week': WEEK_NUMBER,
        'topic': TOPIC,
        'feature': FEATURE_NAME,
        'objectives': LEARNING_OBJECTIVES,
        'complete': is_complete(),
    }

