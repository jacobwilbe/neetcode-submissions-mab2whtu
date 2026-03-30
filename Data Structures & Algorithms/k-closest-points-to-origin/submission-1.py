class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for x,y in points:
            dist = (x**2) + (y**2)
            closest.append([dist, x, y])
        heapq.heapify(closest)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(closest)
            res.append([x,y])
            k -= 1
        return res
