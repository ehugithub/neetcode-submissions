class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(reverse = True)
        # stack holds each car's time to target
        stack = []
        num_cars = len(position)
        res = 0

        for pos, speed in combined:
            time_to_target = (target - pos) / speed
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)

        return len(stack)