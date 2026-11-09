class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))
            else:
                two = stack.pop()
                one = stack.pop()
                if token == "+":
                    stack.append(one + two)
                elif token == "-":
                    stack.append(one - two)
                elif token == "*":
                    stack.append(one * two)
                else:
                    stack.append(int(one / two))
        return stack[0]

        