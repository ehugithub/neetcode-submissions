class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        # store indices
        st = []

        for i, temp in enumerate(temperatures):
            while st and temp > temperatures[st[-1]]:
                j = st.pop()
                answer[j] = i - j
            st.append(i)

        return answer
        