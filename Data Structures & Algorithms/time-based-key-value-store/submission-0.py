class TimeMap:

    def __init__(self):
        # dict: key -> value-timestamp pairs
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = self.d[key]

        left, right = 0, len(l) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if l[mid][0] == timestamp:
                return l[mid][1]
            elif l[mid][0] > timestamp:
                right = mid - 1
            elif mid == len(l) - 1 or l[mid + 1][0] > timestamp:
                return l[mid][1]
            else:
                left = mid + 1

        return ""


