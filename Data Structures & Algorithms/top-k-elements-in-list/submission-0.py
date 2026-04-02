import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums: 
            freq_map[num] = 1+ freq_map.get(num, 0)
        
        max_heap = []
        for num, count in freq_map.items():
            heapq.heappush(max_heap, (-1 * count, num))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res