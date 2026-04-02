class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
        const directions = [[0,1], [0,-1], [1,0], [-1,0]]
        const rows = grid.length
        const cols = grid[0].length
        let fresh_fruits_count = 0
        let mins_count = 0
        let q = []

        for (let r=0; r < rows; r++) {
            for (let c=0; c < cols; c++) {
                if (grid[r][c] === 2) {
                    q.push([r,c])
                }
                if (grid[r][c]=== 1) {
                    fresh_fruits_count++
                }
            }
        }

        while (q.length !== 0) {
            const curr_q_length = q.length
            let has_rotton = false
            for (let i =0; i < curr_q_length; i++) {
                const rotton = q.shift()

                for (let [dr, dc] of directions) {
                    let row = dr + rotton[0]
                    let col = dc + rotton[1]
                    
                    if (row >= 0 && row < rows && col >= 0 && col < cols && grid[row][col] === 1) {
                        grid[row][col] = 2
                        fresh_fruits_count--
                        q.push([row, col])
                        has_rotton = true

                    }
                }
            }
            if (has_rotton) {
                mins_count++
            }
        }

        return fresh_fruits_count === 0 ? mins_count : -1
    }
}
