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

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(10)
            >>> bst.root.value
            10

        Hints:
            Define a helper inside this method:
                def _insert(node, new_value):
                    if node is None: return TreeNode(new_value)
                    if new_value < node.value: node.left = _insert(node.left, new_value)
                    elif new_value > node.value: node.right = _insert(node.right, new_value)
                    return node
            Then call: self.root = _insert(self.root, value)
        """
        # TODO: Use a recursive helper to insert value in the correct position
        pass

    def search(self, value: int) -> bool:
        """Return True if value exists in the tree, False otherwise.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(10)
            >>> bst.search(10)
            True
            >>> bst.search(99)
            False

        Hints:
            current = self.root
            while current is not None:
                if current.value == value: return True
                elif value < current.value: current = current.left
                else: current = current.right
            return False
        """
        # TODO: Walk the tree to find the value
        pass

    def inorder(self) -> list[int]:
        """Return all values in ascending order (left, node, right).

        Example:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15]: bst.insert(v)
            >>> bst.inorder()
            [5, 10, 15]

        Hint:
            def _walk(node):
                if node is None: return []
                return _walk(node.left) + [node.value] + _walk(node.right)
            return _walk(self.root)
        """
        # TODO: Return values in inorder (left → node → right)
        pass

    def preorder(self) -> list[int]:
        """Return values in preorder (node, left, right).

        Hint:
            def _walk(node):
                if node is None: return []
                return [node.value] + _walk(node.left) + _walk(node.right)
            return _walk(self.root)
        """
        # TODO: Return values in preorder (node → left → right)
        pass

    def postorder(self) -> list[int]:
        """Return values in postorder (left, right, node).

        Hint:
            def _walk(node):
                if node is None: return []
                return _walk(node.left) + _walk(node.right) + [node.value]
            return _walk(self.root)
        """
        # TODO: Return values in postorder (left → right → node)
        pass

    def get_height(self) -> int:
        """Return the height of the tree. An empty tree has height 0.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.get_height()
            0
            >>> bst.insert(10)
            >>> bst.get_height()
            1

        Hint:
            def _height(node):
                if node is None: return 0
                return 1 + max(_height(node.left), _height(node.right))
            return _height(self.root)
        """
        # TODO: Compute and return the tree's height recursively
        pass


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

