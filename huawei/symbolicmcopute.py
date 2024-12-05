"""
输入是整数，做加减乘除运算。结果为整数直接输出，为真分数时必须是最简，为假分数时必须化到最简并且不能是带分数
为负数时必须将符号提到最前面

关键点创建两个栈，一个栈存储数值，一个栈存储运算符和左括号
右括号是触发运算的机关，每次运算后更新到数值栈顶并弹出运算符中的左括号，继续下一轮计算
没有括号的运算时，需要继续计算直至运算符的栈为空
在中间计算时，碰上已经存在的运算符优先级高于或等于即将插入栈内的运算符的优先级时，可以先做一次合并中间结果的运算


"""
from fractions import Fraction

def calculate(expression):
   #新建一个函数更新每次遇到右括号后的函数值更新到values的栈顶
    def apply_operator(operators,values):
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        if op == '+': values.append(left + right)
        elif op == '-': values.append(left - right)
        elif op == '*': values.append(left * right)
        elif op == '/':
            if(right==0):
                print('ERROR')
            else:
                values.append(Fraction(left / right))  # 假设除法是浮点除法          
        else: raise RuntimeError('未知操作符')

    #确认计算的优先顺序
    def get_precedence(op):
        if (op in ('+', '-')): return 1
        if (op in ('*', '/')): return 2
        return 0

    operators = [] #操作符和左括号存储
    values = [] #数值存储
    i = 0
    while i < len(expression):
        if(expression[i] == ' '):
            i += 1
            continue
        if(expression[i].isdigit()):#处理数字
            j = i
            #此处是防止数字有多位，而不是只有一位数字的方法
            while (j < len(expression) and expression[j].isdigit()):
                j += 1
            values.append(int(expression[i:j]))
            i = j
        elif(expression[i] =='('): # 处理左括号
            operators.append(expression[i])
            i += 1
        elif(expression[i] in '+-*/'):#处理操作符
            while (operators and operators[-1] != '(' and get_precedence(operators[-1]) >= get_precedence(expression[i])):
                apply_operator(operators,values)
            operators.append(expression[i])
            print("values",values)
            print("operators ))",operators)
            i += 1
        elif(expression[i] ==')'):#处理右括号
            while(operators[-1]!='('):
                apply_operator(operators,values)
            operators.pop()#弹出左括号
            i += 1
        else:
            raise RuntimeError('无效字符')
    #将没有括号的计算值统计出来  
    while operators:
        apply_operator(operators,values) 
    return values[0]

            
        #将括号外的数值计算出来
if __name__ == '__main__':
    expression = "1 + 5 * 7 / 8"
    result = calculate(expression)
    print(result)
