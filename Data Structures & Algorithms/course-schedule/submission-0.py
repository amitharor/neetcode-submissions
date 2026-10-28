'''
Input(s): arr (nested arr), numCourses (int)
Output: bool; return True if possible to finish all course, otherwise return False

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
prerequisites[i].length == 2
0 <= a[i], b[i] < numCourses
All prerequisite pairs are unique.

Approach:
dfs

Time: O()
Space: O()
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting: # Cycle detection
                return False

            if graph[course] == []:
                return True

            visiting.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True