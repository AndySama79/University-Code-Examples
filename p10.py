def operate(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return int(op1 / op2)
def calculate(*args):
    num = []
    op = []
    for element in args:
        if element == '+' or element == '-' or element == '/' or element == '*':
            op.append(element)
        else:
            num.append(element)
    
    while len(op) != 0 and len(num) >= 2:
        n1 = num[0]
        n2 = num[1]
        ope = op[0]
        res = operate(n1, n2, ope)
        if len(num) != 2:
            num = [res] + num[2:]
        else:
            num = [res]
        if len(op) != 1:
            op = op[1:]
        else:
            op = []
    
    return num[0]

#print(calculate(2, '+', 3, '*', 5, '-', 3, '*', 4, '+', -6, '/', 11))
print(calculate(2, "+", 3, "*", 5, "-", 3, '*', 4, '+', -6, '/', 11))


