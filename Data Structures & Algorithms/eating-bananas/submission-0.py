class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Use binary search to determine the `k` minimum bananas you can eat within `h` hours
        l = 1
        r = max(piles)
        `k` would be the midpoint of `l` and `r`
        Iterate through piles to see if the total time it takes to eat with `k` exceeds `h`
        If so, l = k + 1
        Else, update res = k, r = k - 1
        '''

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2

            time_required = 0
            for p in piles:
                time_required += math.ceil(p / k)
            
            if time_required > h:
                l = k + 1
            else:
                res = k
                r = k - 1

        return res