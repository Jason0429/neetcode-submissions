class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict() # value : count

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        heap = []
        for value, freq in count.items():
            heap.append((-freq, value))
        
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            _, value = heapq.heappop(heap)
            res.append(value)

        return res