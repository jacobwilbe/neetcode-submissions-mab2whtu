class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, subset, remaining):
            if i < len(nums) and remaining == 0:
                result.append(subset.copy())
                return
            if i >= len(nums) or remaining < 0:
                return
            subset.append(nums[i])
            dfs(i, subset, remaining - nums[i])
            subset.pop()
            dfs(i + 1, subset, remaining)
        dfs(0, [], target)
        return result
            
