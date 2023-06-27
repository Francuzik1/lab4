total = []
stack = []
priority = {')': 0, '+': 1, '-': 1, '/': 2, '*': 2, '^': 3}
exp = input("Enter Infix Expression:-")
for ch in exp[::-1]:
    if ch == ")":
        stack.append(ch)
    elif ch == "(":
        while stack[-1] != ")":
            ele = stack.pop()
            total.append(ele)
        stack.pop()
    elif ch == '^' or ch == '/' or ch == '%' or ch == '+' or ch == '-' or ch == '*':
        if len(stack) > 0:
            while priority[stack[-1]] > priority[ch]:
                ele = stack.pop()
                total.append(ele)
                if len(stack) == 0:
                    break
        stack.append(ch)
    else:
        total.append(ch)
if len(stack) > 0:
    while len(stack) != 0:
        ele = stack.pop()
        total.append(ele)
print(''.join(list(reversed(total))))
