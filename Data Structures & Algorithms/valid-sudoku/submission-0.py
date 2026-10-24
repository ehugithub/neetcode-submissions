class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num.isnumeric():
                    num = int(num)
                else:
                    continue
                box_id = (r // 3) * 3 + (c // 3)
                if num in rows[r] | cols[c] | boxes[box_id]:
                    return False
                else:
                    for d in rows[r], cols[c], boxes[box_id]:
                        d.add(num)
        
        return True

        