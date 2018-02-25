#Given a binary tree, return all root-to-leaf paths.
'''
For example, given the following binary tree:
   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:
["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        return ['{}->{}'.format(root.val, p)
                for subtree in (root.left, root.right) if subtree
                for p in self.binaryTreePaths(subtree)]


"""
Test cases
1) []
Empty tree. The root is a reference to NULL (C/C++), null (Java/C#/Javascript), None (Python), or nil (Ruby).

2) [1,2,3]
       1
      / \
     2   3

3) [1,null,2,3]
       1
        \
         2
        /
       3

4) [5,4,7,3,null,2,null,-1,null,9]
       5
      / \
     4   7
    /   /
   3   2
  /   /
 -1  9

 """
