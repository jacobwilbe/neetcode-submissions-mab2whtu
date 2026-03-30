class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums.sort()
        path = []
        def dfs(i):
            res.append(path[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return res

