class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            l = len(string)
            res += str(l) + '#' + string
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            num = ""
            while s[i].isnumeric():
                num += s[i]
                i += 1
            num = int(num)

            # skip hashtag
            i += 1

            res.append(s[i : i + num])
            i += num
        return res
