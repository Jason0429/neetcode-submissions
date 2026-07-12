class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Build adjacency list graph course: [prereqs]
        If cycle detected, return []
        Otherwise, build path through DFS and keeping a visited set
        to mark visited courses along the current DFS path
        '''

        course_to_prereqs = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            course_to_prereqs[course].append(prereq)
        
        res = []
        visited = set()
        cycles = set()

        def dfs(course):
            if course in cycles:
                return False
            
            if course in visited:
                return True

            # we want to add to cycle and then traverse entire DFS path to see if same course is on the same path more than once
            cycles.add(course)
            for prereq in course_to_prereqs[course]:
                if not dfs(prereq):
                    return False
            
            # remove course from cycles set once path is done traversing
            cycles.remove(course)

            # add course to visited once we have completed a non-cyclic path so we do not have to traverse again
            visited.add(course)

            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
            
        