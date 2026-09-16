class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers) - 1

        while numbers[low] + numbers[high] != target:
            total = numbers[low] + numbers[high]
            if total < target:
                low += 1
            else:
                high -= 1

        return [low + 1, high + 1]


        