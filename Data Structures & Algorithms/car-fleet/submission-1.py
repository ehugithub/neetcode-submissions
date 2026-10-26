class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = sorted(list(zip(position, speed)), reverse = True)

        for pos, spd in pairs:
            time_to_reach = (target - pos) / spd

            if stack and stack[-1] >= time_to_reach:
                continue

            stack.append(time_to_reach)

        return len(stack)
        