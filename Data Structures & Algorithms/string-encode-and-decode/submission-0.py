class Solution:

    def encode(self, strs: List[str]) -> str:
        # len + # + (string)
        res = ""

        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j].isnumeric():
                j += 1
            
            length = int(s[i : j])
            
            # skip hashtag
            j += 1

            res.append(s[j : j + length])

            i = j + length
        
        return res


