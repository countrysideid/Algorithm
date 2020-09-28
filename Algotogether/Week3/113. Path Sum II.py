# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def recurseTree(node, remainSum, pathNodes, pathList):
            if not node:
                return
            pathNodes.append(node.val)
            
            if remainSum == node.val and not node.left and not node.right:
                pathList.append(list(pathNodes))
            else:
                recurseTree(node.left, remainSum - node.val, pathNodes, pathList)
                recurseTree(node.right, remainSum - node.val, pathNodes, pathList)
            pathNodes.pop()
            
        pathsList = []
        recurseTree(root, sum, [], pathsList)
        return pathsList
