from fractions import Fraction

def calculate(expression):
    def apply_operator(operators, values):
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        if op == '+': values.append(left + right)
        elif op == '-': values.append(left - right)
        elif op == '*': values.append(left * right)
        elif op == '/': values.append(Fraction(left / right))  # 假设除法是浮点除法
        else: raise RuntimeError('未知操作符')

    operators = []  # 存储操作符和左括号
    values = []     # 存储操作数
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i].isdigit():  # 处理数字
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j
        elif expression[i] == '(':  # 处理左括号
            operators.append(expression[i])
            print("operators (",operators)
            i += 1
        elif expression[i] in '+-*/':  # 处理操作符
            while (operators and operators[-1] != '(' and get_precedence(operators[-1]) >= get_precedence(expression[i])):
                apply_operator(operators, values)
            print("operators +-*/ ",operators)
            operators.append(expression[i])
            print(operators)
            i += 1
        elif expression[i] == ')':  # 处理右括号
            print("operators )",operators)
            while operators[-1] != '(':
                if(operators[-1]=='/' and values[-1]==0):
                    print('ERROR')
                    break
                apply_operator(operators, values)
            print("operators ))",operators)
            operators.pop()  # 弹出左括号
            i += 1
        else:
            raise RuntimeError('无效字符')
    #这个操作是运算的值不在最外层的括号内的计算
    while operators:
        apply_operator(operators, values)
        print(operators)
    
    return values[0]

def get_precedence(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    return 0

# 测试表达式
expression = "1 * (3 * 4 / (8 - (7 + 1)))"
result = calculate(expression)
print(f"表达式的结果是: {result}")