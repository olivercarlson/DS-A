class Solution:
    # SOLUTION #1: Kahn's Algorithm for Topological Sorting
    # TC: O(N+M) - iterate through all prerequisites and number of courses
    # SC: O(N+M) - deque can store all courses + prerequisites.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for pr in prerequisites:
            indegree[pr[0]] += 1
            adj[pr[1]].append(pr[0])

        d = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                d.appendleft(i)
        coursesTaken = 0
 
        while d:
            if coursesTaken >= numCourses:
                return True
            cur = d.popleft()
            coursesTaken += 1
            for course_idx in adj[cur]:
                indegree[course_idx] -= 1
                if indegree[course_idx] == 0:
                    d.append(course_idx)

        return coursesTaken >= numCourses
