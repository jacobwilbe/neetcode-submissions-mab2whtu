class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for pre in prerequisites:
            preMap[pre[0]].append(pre[1])
        

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
