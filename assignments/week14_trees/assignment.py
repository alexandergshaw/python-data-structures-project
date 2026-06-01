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
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        def _insert(node: TreeNode | None, new_value: int) -> TreeNode:
            if node is None:
                return TreeNode(new_value)
            if new_value < node.value:
                node.left = _insert(node.left, new_value)
            elif new_value > node.value:
                node.right = _insert(node.right, new_value)
            return node
        self.root = _insert(self.root, value)

    def search(self, value: int) -> bool:
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def inorder(self) -> list[int]:
        def _walk(node: TreeNode | None) -> list[int]:
            if node is None:
                return []
            return _walk(node.left) + [node.value] + _walk(node.right)
        return _walk(self.root)

    def preorder(self) -> list[int]:
        def _walk(node: TreeNode | None) -> list[int]:
            if node is None:
                return []
            return [node.value] + _walk(node.left) + _walk(node.right)
        return _walk(self.root)

    def postorder(self) -> list[int]:
        def _walk(node: TreeNode | None) -> list[int]:
            if node is None:
                return []
            return _walk(node.left) + _walk(node.right) + [node.value]
        return _walk(self.root)

    def get_height(self) -> int:
        def _height(node: TreeNode | None) -> int:
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
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

