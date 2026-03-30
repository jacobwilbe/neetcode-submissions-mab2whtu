class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            diff = target - nums[i]
            hashmap[diff] = i
        return []
         