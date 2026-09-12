class Solution:
    def isHappy(self, n: int) -> bool:
        def calcSum(n: int) -> int:
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                print(res)
                n = n // 10
            return res
        s = {n}

        while n > 1:
            n = calcSum(n)
            if n in s:
                return False
            else:
                s.add(n)
        return True
        