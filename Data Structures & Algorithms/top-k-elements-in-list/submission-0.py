class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = dict()

        for n in nums:
            num_to_freq[n] = num_to_freq.get(n, 0) + 1
        
        heap = []

        for num, freq in num_to_freq.items():
            heapq.heappush(heap, (-freq, num))

        res = [0] * k
        for i in range(k):
            _, n = heapq.heappop(heap)
            res[i] = n

        return res