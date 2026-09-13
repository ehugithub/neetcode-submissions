class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxFreq = max(counts.values())
        numMax = sum(1 for v in counts.values() if v == maxFreq)

        skeleton = (maxFreq - 1) * (n + 1) + numMax
        return max(skeleton, len(tasks))

        return 0
        