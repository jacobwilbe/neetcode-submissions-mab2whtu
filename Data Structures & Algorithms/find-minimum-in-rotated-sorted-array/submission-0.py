class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid_index = (l+r) // 2
            res = min(res, nums[mid_index])
            if nums[mid_index] >= nums[l]:
                l = mid_index + 1
            else:
                r = mid_index - 1
        return res
