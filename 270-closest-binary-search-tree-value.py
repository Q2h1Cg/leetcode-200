class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            closest = min(root.val, closest, key=lambda x: abs(x - target))
            root = root.left if root.val > target else root.right

        return closest
