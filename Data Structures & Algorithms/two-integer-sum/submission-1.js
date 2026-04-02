class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let sortedNums = []
        for(let i = 0;  i < nums.length; i++) {
            sortedNums.push([nums[i], i])
        }

        sortedNums.sort((a,b) => a[0] - b[0])

        let l = 0
        let r = nums.length -1

        while (l < r) {
            const sum = sortedNums[l][0] + sortedNums[r][0]
            if (sum === target) {
                return [sortedNums[l][1], sortedNums[r][1]]
            }

            if (sum < target) {
                l++
            } else {
                r--
            }
        }
        return []
    }
}
