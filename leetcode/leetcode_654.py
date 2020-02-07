from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        def construct_tree(nums):
            idx = nums.index(max(nums))
            root = TreeNode(nums[idx])

            if len(nums[idx+1:]) > 0:
                root.right = construct_tree(nums[idx+1:])
            if len(nums[0:idx]) > 0:
                root.left = construct_tree(nums[0:idx])
            
            return root

        return construct_tree(nums)


sol = Solution2()
nums = [3,2,1,6,0,5]
res = sol.constructMaximumBinaryTree(nums)

print(res.val)
print(res.left.val)
print(res.left.right.val)
print(res.left.right.left.val)
print(res.right.val)
print(res.right.left.val)
        