#!/usr/bin/python
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = [];
        for t in tokens:
            if (t == '+'):
                a = stack.pop()
                b = stack.pop()
                c = a + b;
                stack.append(c)
            elif (t == '-'):
                a = stack.pop()
                b = stack.pop()
                c = b - a;
                stack.append(c)
            elif (t == '*'):
                a = stack.pop()
                b = stack.pop()
                c = a * b;
                stack.append(c)
            elif (t == '/'):
                a = stack.pop()
                b = stack.pop()
                c = int(float(b) / float(a));
                stack.append(c)
            else:
                stack.append(int(t))
        return stack.pop()


sol = Solution()
q0 = ["2", "1", "+", "3", "*"]
q1 = ["4", "13", "5", "/", "+"]
q2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] #22
#print sol.evalRPN(q0)
#print sol.evalRPN(q1)
print sol.evalRPN(q2)



