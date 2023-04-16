class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = root.val - target

        # 当前节点值等于目标值
        # 或当前节点值小于目标值且没有右节点
        # 或当前节点值大于目标值且没有左节点
        if diff == 0 \
                or (diff < 0 and not root.right) \
                or (diff > 0 and not root.left):
            return root.val

        # 当前节点值小于目标值，对比右侧节点查找结果
        if diff < 0:
            right_closest = self.closestValue(root.right, target)
            if abs(diff) <= abs(right_closest - target):
                return root.val

            return right_closest

        # 当前节点值大于目标值，对比左侧节点查找结果
        left_closest = self.closestValue(root.left, target)
        if abs(diff) < abs(left_closest - target):
            return root.val

        return left_closest
