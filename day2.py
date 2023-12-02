import re
def p1():
    sum = 0
    d = {}
    with open('./data/day2.txt') as f:
        data = f.read().split('\n')
        regex = re.compile(r'(\d+) (\w+)')
        for line in data:
            if len(line) == 0:
                continue
            game, line = line.split(': ')
            game = int(game.split(' ')[1])
            for round in line.split(';'):
                r = 0
                g = 0
                b = 0
                for rgb in round.split(','):
                    rgb = rgb.strip()
                    matches = re.findall(regex, rgb)[0]
                    if matches[1] == 'red':
                        r = max(r, int(matches[0]))
                    elif matches[1] == 'green':
                        g = max(g, int(matches[0]))
                    elif matches[1] == 'blue':
                        b = max(b, int(matches[0]))
                if game not in d:
                    d[game] = (r, g, b)
                else:
                    r1, g1, b1 = d[game]
                    d[game] = (max(r, r1), max(g, g1), max(b, b1))
    for k, v in d.items():
        if v[0] <= 12 and v[1] <= 13 and v[2] <= 14:
            sum += k
    
    print(sum)
    return d

def p2():
    d = p1()
    sum = 0
    for v in d.values():
        sum += v[0] * v[1] * v[2]
    print(sum)
p2()