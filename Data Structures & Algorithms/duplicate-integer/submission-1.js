class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const nums_set = new Set()

        for (const num of nums) {
            if (nums_set.has(num)){
                return true
            }
            nums_set.add(num)
        }
        return false
    }
}
