class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false
        } 
        
        let s_arr = s.split("")
        let t_arr = t.split("")

        s_arr.sort((a,b) => a.localeCompare(b))
        t_arr.sort((a,b) => a.localeCompare(b))

        console.log(s_arr, t_arr)
        for (let i = 0; i < s.length; i++) {
            if (s_arr[i] !== t_arr[i]) {
                return false
            }
        }
        return true
    }
}
