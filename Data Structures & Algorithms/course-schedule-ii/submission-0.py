'''
Input(s): prereqs (nest arr - int), numCourse (int)
Output: return order of courses you can take, else return empty array if not possible to finishe all courses

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.

Approach:
DFS - topological sort

Time: O(V + E) - where V is the number of courses and E is the number of prerequisites
Space: O(V + E)
'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for next, prereq in prerequisites:
            indegree[next] += 1
            adj[prereq].append(next)

        output = []

        def dfs(node):
            output.append(node)
            indegree[node] -= 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    dfs(neighbor)

        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)

        return output if len(output) == numCourses else []