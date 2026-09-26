class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []

        # kahn's again
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        while(q):
            node = q.popleft()
            res.append(node)

            for nbr in graph[node]:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    q.append(nbr)

        return res if len(res) == numCourses else []

        