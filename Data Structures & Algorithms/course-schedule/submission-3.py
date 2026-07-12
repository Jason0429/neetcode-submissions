class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Build topological sort dictionary from course: [prereqs]
        Given a pair course to prereq (C, P), if C in prereqs[P], return False because that is not possible
        return True at the end
        '''
        course_to_prereqs = { i: [] for i in range(numCourses) }

        for course, prereq in prerequisites:
            course_to_prereqs[course].append(prereq)

        # visited keeps track of all courses along the current DFS path
        def dfs(course, visited):
            # loop was detected along the current DFS path
            if course in visited:
                return False
            
            # no prerequisites for this course
            if len(course_to_prereqs[course]) == 0:
                return True
            
            visited.add(course)
            for prereq in course_to_prereqs[course]:
                # if one course cannot be completed, return False entirely
                if not dfs(prereq, visited):
                    return False
            
            # we know that this course can be completed so clear to prevent repeat in future
            course_to_prereqs[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        
        return True

        

