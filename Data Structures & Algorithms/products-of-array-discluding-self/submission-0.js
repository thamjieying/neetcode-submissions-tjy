class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const forward = Array(nums.length).fill(1)
        const backwards = Array(nums.length).fill(1)
        for (let i =1; i < nums.length; i++) {
            forward[i] = nums[i-1] * forward[i-1]
        }
        for (let i = nums.length-2 ; i >=0; i--) {
            console.log(i, nums[i+1])
            backwards[i] = backwards[i+1] * nums[i+1]
        }
        const res = []
        for (let i = 0; i < nums.length; i++) {
            res.push(forward[i]*backwards[i])
        }
        return res
    }
}
