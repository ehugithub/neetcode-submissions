class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # min heap 1: to be picked up, sort by from_i
        # min heap 2, to be dropped off, sort by to_i

        numPass = 0
        curDist = 0

        # from_i, to_i, num_i
        future = [(trip[1], trip[2], trip[0]) for trip in trips]
        heapq.heapify(future)
        # to_i, from_i, numPassengers
        inCar = []

        while future:
            # offload passengers
            curDist = future[0][0]
            while inCar and inCar[0][0] <= curDist:
                _, num = heapq.heappop(inCar)
                numPass -= num
            while future and future[0][0] <= curDist:
                from_i, to_i, num_i = heapq.heappop(future)
                numPass += num_i
                if numPass > capacity: return False 
                heapq.heappush(inCar, (to_i, num_i))

        return True     