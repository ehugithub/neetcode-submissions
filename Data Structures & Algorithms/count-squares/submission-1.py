class CountSquares:

    def __init__(self):
        # maintain a hashmap of x and y coords
        # y -> number of pts with that y coord
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) in self.points:
            self.points[(x, y)] += 1
        else:
            self.points[(x,y)] = 1
        

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0

        for (x2, y2), count in self.points.items():
            if x2 != x1 or y2 == y1:
                continue
            
            length = abs(y2 - y1)
            for x3 in [x1 - length, x1 + length]:
                if (x3, y1) in self.points and (x3, y2) in self.points:
                    res += count * self.points[(x3, y1)] * self.points[(x3, y2)]
        return res
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)