class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict that maps val : count of val
        # create a max-heap where highest count val is at the top
        # heap item (count, val)

        freq = dict()
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        heap = []
        for val, count in freq.items():
            heap.append((-count, val))
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            (_, val) = heapq.heappop(heap)
            res.append(val)
        
        return res