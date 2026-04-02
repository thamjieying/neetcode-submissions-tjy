class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length
        const res = Array(n).fill(1)

        for (let i =1; i< n; i++) {
            res[i] = nums[i-1] * res[i-1]
        }

        let postfix = 1
        for (let i = n-1; i >= 0; i--) {
            res[i] *= postfix
            postfix*= nums[i]
        }
        return res
    }
}
