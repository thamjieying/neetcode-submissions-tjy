class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let l = 0
        let max_len = 0
        const set = new Set()


        for (let r =0; r < s.length; r++) {
            while (set.has(s[r])){
                set.delete(s[l])
                l++
            }
            set.add(s[r])
            let string_len = r-l+1
            if (max_len < string_len) {
                max_len = string_len
            }
        }

        return max_len

    }
}
