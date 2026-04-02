class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l = 0,
            r = heights.length-1,
            maxWater = 0
        
        while (l < r) {
            const waterAmt = Math.min(heights[l], heights[r]) * (r-l)
            maxWater = Math.max(maxWater, waterAmt)

            if (heights[l] < heights[r]) {
                l++
            } else {
                r--
            }
        }
        return maxWater

    }
}
