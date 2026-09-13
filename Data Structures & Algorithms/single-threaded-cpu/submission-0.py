class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # heap 1: tasks to be available in the future, sorted by enqueueTime
        # heap 2: available tasks, sorted by processing time

        for idx, task in enumerate(tasks):
            task.append(idx)

        futureTasks = tasks
        availTasks = []
        res = []
        time = 1
        heapq.heapify(futureTasks)

        while futureTasks or availTasks:
            # if cpu will be idle for a long time:
            if not availTasks and futureTasks[0][0] > time:
                time = futureTasks[0][0]
            while futureTasks and futureTasks[0][0] <= time:
                eq, pt, idx = heapq.heappop(futureTasks)
                heapq.heappush(availTasks, (pt, idx))

            pt, idx = heapq.heappop(availTasks)
            res.append(idx)
            time += pt

        return res
        

        