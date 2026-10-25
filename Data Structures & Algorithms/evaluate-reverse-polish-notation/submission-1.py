class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                stack.append(int(t))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            if t == '+':
                stack.append(num1 + num2)
            elif t == '-':
                stack.append(num1 - num2)
            elif t == '*':
                stack.append(num1 * num2)
            elif t == '/':
                stack.append(int (num1 / num2))
        return stack[-1]
            

        