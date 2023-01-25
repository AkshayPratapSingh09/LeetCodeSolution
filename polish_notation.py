def evalRPN(tokens):
        operations = {
            "*": lambda x,y: x*y,
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: float(x)/y
        }
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                print("token is number\n",stack)
            else:
                right = stack.pop()
                left = stack.pop()
                print("token is Operation",token)
                print("left-> ",left,"Right-> ",right)
                result = operations[token](left, right)
                stack.append(int(result))
                print(stack)
        return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))