def calc():
    result = None
    while True:
        expression = (yield result)
        if expression:
            try:
                values = expression.split()
                operand1 = int(values[0])
                operator = values[1]
                operand2 = int(values[2])

                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                elif operator == '*':
                    result = operand1 * operand2
                elif operator == '/':
                    result = operand1 / operand2
                else:
                    result = 'Invalid operator'

            except (ValueError, IndexError, ZeroDivisionError) as e:
                print(e)
        
expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
