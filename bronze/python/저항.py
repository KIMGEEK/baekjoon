black = {'key': 0, 'value': 1}
brown = {'key': 1, 'value': 10}
red = {'key': 2, 'value': 100}
orange = {'key': 3, 'value': 1000}
yellow = {'key': 4, 'value': 10000}
green = {'key': 5, 'value': 100000}
blue = {'key':6, 'value': 1000000}
violet = {'key':7, 'value': 10000000}
grey = {'key':8, 'value': 100000000}
white = {'key':9, 'value': 1000000000}

q = []
for i in range(3):
    q.append(input())
    
result = []
for i in range(len(q)):
    if q[i] == 'black':
        result.append(black)
    elif q[i] == 'brown':
        result.append(brown)
    elif q[i] == 'red':
        result.append(red)
    elif q[i] == 'orange':
        result.append(orange)
    elif q[i] == 'yellow':
        result.append(yellow)
    elif q[i] == 'green':
        result.append(green)
    elif q[i] == 'blue':
        result.append(blue)
    elif q[i] == 'violet':
        result.append(violet)
    elif q[i] == 'grey':
        result.append(grey)
    elif q[i] == 'white':
        result.append(white)

a = (result[0]['key']*10 + result[1]['key'])*result[2]['value']

print(a)
