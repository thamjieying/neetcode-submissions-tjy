/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isValidBST(root, minVal = -Infinity, maxVal=Infinity) {
        if(!root) {
            return true
        }

        if(root.val <= minVal || root.val >= maxVal) {
            return false
        }

        return this.isValidBST(root.left, minVal, root.val) && this.isValidBST(root.right, root.val, maxVal)
    }
}
