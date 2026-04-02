class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length=== 0){
            return 0
        }
        nums.sort((a,b) => a-b)
        let maxStreak = 1
        
        let streak = 0
        let prevNum = null
        for (let num of nums) {
            console.log("num", num)
            if (prevNum === null){
                prevNum = num
                streak++
            }else if (prevNum == num) {
                continue
            } else if (num - prevNum === 1) {
                streak++
                maxStreak = Math.max(maxStreak, streak)
                prevNum = num
            } else {
                streak = 1
                prevNum = num
            }
            console.log("streak", streak)
        }
        return maxStreak
    }
}
