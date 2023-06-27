oper = ['+', '-', '*', '/', '(', ')', '^']
oper_val = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def inpofix(valden):
    stack = []
    total = ''
    for work in valden:
        if work not in oper:
            total += work
        elif work == '(':
            stack.append('(')
        elif work == ')':
            while stack and stack[-1] != '(':
                total += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and oper_val[work] <= oper_val[stack[-1]]:
                total += stack.pop()
            stack.append(work)
    while stack:
        total += stack.pop()

    print(total)


inpofix("4+4*4")
