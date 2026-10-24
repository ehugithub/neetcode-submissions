class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))

            sorted_strings[s_sorted].append(s)

        return list(sorted_strings.values())
        