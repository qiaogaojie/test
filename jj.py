def calculate(x, y, add):
    temp = add
    if ord(x) > ord(y):
        x, y = y, x
    if x == '/':
        if y == '@':
            temp += 13
        elif y == '#':
            temp += 4
    elif x == '#':
        if y == '#':
            temp += 5
        else:
            temp += 20
    elif x == '@':
        temp += 7
    else:
        temp += int(x)
        temp += int(y)
    add_new = temp // 10
    ans = temp % 10
    return add_new, str(ans)

def calculate_int(x, y, add_new):
    temp_int = ''
    m, n = len(x_int), len(y_int)
    if m > n:
        for i in range(1, n+1):
            add_new, ans = calculate(x_int[-i], y_int[-i], add_new)
            temp_int = ans + temp_int
        temp_int = x_int[:-n] + temp_int
    else:
        for i in range(1, m+1):
            add_new, ans = calculate(x_int[-i], y_int[-i], add_new)
            temp_int = ans + temp_int
        temp_int = y_int[:-m] + temp_int
    return temp_int

n = int(input())
data = input().split('+')
x = data[0].split('.')
y = data[1].split('.')
temp_decimal = ''
if len(x) == 2 and len(y) == 2:
    x_decimal, x_int = x[1], x[0]
    y_decimal, y_int = y[1], y[0]
    m, n = len(x_decimal), len(y_decimal)
    if m > n:
        temp_decimal = x[1][n:]
    else:
        temp_decimal = y[1][m:]
    less, add_new = min(m, n), 0
    for i in range(less - 1, -1, -1):
        add_new, ans = calculate(x_decimal[i], y_decimal[i], add_new)
        temp_decimal = ans + temp_decimal
    temp_int = calculate_int(x_int, y_int, add_new)
elif len(x) == 2 and len(y) == 1:
    x_decimal, x_int = x[1], x[0]
    y_int = y[0]
    temp_decimal = x_decimal
    temp_int = calculate_int(x_int, y_int, 0)
elif len(y) == 2 and len(x) == 1:
    y_decimal, y_int = y[1], y[0]
    x_int = x[0]
    temp_decimal = y_decimal
    temp_int = calculate_int(x_int, y_int, 0)
else:
    x_int = x[0]
    y_int = y[0]
    temp_int = calculate_int(x_int, y_int, 0)
print(eval(temp_int + '.' + temp_decimal))
    