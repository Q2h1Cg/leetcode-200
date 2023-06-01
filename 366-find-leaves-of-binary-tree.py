class Solution:
    def dfs(self, node, ans):
        if not node:
            return -1

        left = self.dfs(node.left, ans)
        right = self.dfs(node.right, ans)
        depth = max(left, right) + 1

        if depth >= len(ans):
            ans.append([])

        ans[depth].append(node.val)

        return depth

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.dfs(root, ans)
        return ans
