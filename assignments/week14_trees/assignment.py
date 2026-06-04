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

        """
        def _insert(node, new_value):
            if node is None:
                return TreeNode(new_value)
            if new_value < node.value:
                node.left = _insert(node.left, new_value)
            elif new_value > node.value:
                pass  # TODO
            return node
        self.root = _insert(self.root, value)

    def search(self, value: int) -> bool:
        """Return True if value exists in the tree, False otherwise.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.insert(10)
            >>> bst.search(10)
            True
            >>> bst.search(99)
            False

        """
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif value < current.value:
                current = None  # TODO
            else:
                current = None  # TODO
        return False

    def inorder(self) -> list[int]:
        """Return all values in ascending order (left, node, right).

        Example:
            >>> bst = BinarySearchTree()
            >>> for v in [10, 5, 15]: bst.insert(v)
            >>> bst.inorder()
            [5, 10, 15]

        """
        def _walk(node):
            if node is None:
                return []
            return None  # TODO
        return _walk(self.root)

    def preorder(self) -> list[int]:
        """Return values in preorder (node, left, right).

        """
        def _walk(node):
            if node is None:
                return []
            return None  # TODO
        return _walk(self.root)

    def postorder(self) -> list[int]:
        """Return values in postorder (left, right, node).

        """
        def _walk(node):
            if node is None:
                return []
            return None  # TODO
        return _walk(self.root)

    def get_height(self) -> int:
        """Return the height of the tree. An empty tree has height 0.

        Example:
            >>> bst = BinarySearchTree()
            >>> bst.get_height()
            0
            >>> bst.insert(10)
            >>> bst.get_height()
            1

        """
        def _height(node):
            if node is None:
                return 0
            return None  # TODO
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

