class Solution:
    def reverseBits(self, n: int) -> int:
        # bit at position i ends up at position 31 - i

        # res = 00000000...
        res = 0

        for _ in range(32):
            # get right most bit of n
            bit = n & 1
            # set right most bit to res: shift up 1 bit each time
            res = (res << 1) | bit
            n >>= 1
        return res
        