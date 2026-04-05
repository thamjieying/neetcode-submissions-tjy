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
     * @return {number[][]}
     */
    levelOrder(root) {
        if (!root) {
            return []
        }

        const q = [root]
        const res = []
        while (q.length) {
            const levelCount = q.length
            const level = []
            for (let i = 0; i < levelCount; i++) {
                const node = q.shift()
                level.push(node.val)
                if (node.left) {
                    q.push(node.left)
                }
                if (node.right) {
                    q.push(node.right)
                }
            }
            res.push(level)
        }
        return res
    }
}
