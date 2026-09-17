class TimeMap:

    def __init__(self):
        # dict: key -> (value, timestamp): timestamp is increasing, so will already be sorted
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d.setdefault(key, []).append((value, timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        l = self.d[key]
        left = 0
        right = len(l)

        while left < right:
            mid = left + (right - left) // 2
            val, ts_prev = l[mid]
            if ts_prev == timestamp:
                return val
            if ts_prev < timestamp:
                left = mid + 1
            else:
                right = mid
        return l[left - 1][0] if left > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)