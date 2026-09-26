class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # need to check if there is a cycle, let's use kahn's
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        # create the graph

        for course, prereq in prerequisites:
            #[1, 0]: 0 --> 1
            graph[prereq].append(course)
            indegrees[course] += 1

        q = deque()
        # add courses with zero indegree
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)
        #process courses

        completed = 0
        while q:
            node = q.popleft()
            completed += 1

            nbrs = graph[node]
            for nbr in nbrs:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    q.append(nbr)

        return completed == numCourses 