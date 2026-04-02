class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const frequency_map = {}
        for (let num of nums) {
            frequency_map[num] = (frequency_map[num] || 0) + 1
        }

        const arr = Object.entries(frequency_map)
            .map(([num, freq]) => [freq, parseInt(num)])
            .sort((a,b) => b[0]-a[0])
        return arr.slice(0,k).map((pair) => [pair[1]])
    }
}
