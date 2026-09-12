class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            sort = "".join(sorted(s))

            if sort in d.keys():
                d[sort].append(s)
            else:
                d[sort] = [s]
        return list(d.values())
        