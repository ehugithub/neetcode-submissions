class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {")": "(", "}": "{", "]": "["}

        st = []

        for ch in s:
            if ch in mappings.keys():
                if len(st) == 0: return False
                if mappings[ch] != st.pop(): return False
            else:
                st.append(ch)


        return len(st) == 0