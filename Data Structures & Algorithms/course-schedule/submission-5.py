class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Initialize mapping (course to prereqs) course : []
        Build the map
        DFS from each course, if course can be completed, change prereqs to [] to mark
        Keep a visited set as you DFS to detect loop, if detected, return False
        '''

        crs_to_prs = { c: [] for c in range(numCourses) }

        for crs, pr in prerequisites:
            crs_to_prs[crs].append(pr)

        # can this course be completed?
        def dfs(course, visited):
            # if loop, cannot be completed
            if course in visited:
                return False
            
            # no prerequisites, can be completed
            if not crs_to_prs[course]:
                return True
            
            visited.add(course)
            for pr in crs_to_prs[course]:
                if not dfs(pr, visited):
                    return False
            crs_to_prs[course] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        
        return True
        
