class Solution:
    def countBits(self, n: int) -> list[int]:
        # powers of 2: always 1

        bits = [0] * (n + 1)

        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)

        return bits
        