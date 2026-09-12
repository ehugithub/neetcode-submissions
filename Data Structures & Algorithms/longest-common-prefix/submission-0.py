class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the list: that would group all the common prefixes together
        # this way, only have to compare the first and last strings
        strs.sort()

        return "".join(c1 for c1, c2 in takewhile(lambda x: x[0] == x[1], zip(strs[0], strs[len(strs) - 1])))
        