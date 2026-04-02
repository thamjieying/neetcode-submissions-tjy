class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const q = []
        const map = { 
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        for (let char of s) {
            if (Object.keys(map).includes(char)) {
                q.push(char)
            } else {
                const start_bracket = q.pop()
                if (map[start_bracket] !== char) {
                    return false
                }
            }
        }
        return q.length === 0
    }
}
