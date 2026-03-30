class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i, subset, remaining):
            if remaining == 0:
                result.append(subset.copy())
                return
            
            for j in range(i, len(nums)):
                if remaining - nums[j] < 0:
                    return
                subset.append(nums[j])
                dfs(j, subset, remaining - nums[j])
                subset.pop()
            
        dfs(0, [], target)
        return result
            
