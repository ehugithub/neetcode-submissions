class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        counts = Counter(s)
        heap = [(-count, ch) for ch, count in counts.items()]

        heapq.heapify(heap)

        most_recent = ""

        while heap:
            count, letter = heapq.heappop(heap)
            if letter != most_recent:
                res += letter
                if count < -1:
                    heapq.heappush(heap, (count + 1, letter))
                most_recent = letter
            else:
                if not heap:
                    return ""
                temp_c, temp_l = heapq.heappop(heap)
                res += temp_l
                most_recent = temp_l
                if temp_c < -1:
                    heapq.heappush(heap, (temp_c + 1, temp_l))
                heapq.heappush(heap, (count, letter))

        return res


        