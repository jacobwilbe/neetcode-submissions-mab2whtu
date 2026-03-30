class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        currMax = 0
        l = 0

        for r in range(k, len(nums) + 1):
            currMax = max(nums[l:r])
            maxes.append(currMax)
            l += 1
        return maxes
            
