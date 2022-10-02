# Треугольник смотрящий вправо:

q = int(input('Введите число: '))

for w in range(0, q):
    for e in range(0, w + 1):
        print('*', end=' ')
    print()
for r in range(q, 0, -1):
    for t in range(0, r):
        print('*', end=' ')
    print()

# Треугольник смотрящий влево:

q1 = int(input('Введите число: '))

for w1 in range(0, q1):
    for a in range(w1, q1 - 1):
        print(' ', end=' ')
    for e1 in range(0, w1 + 1):
        print('*', end=' ')
    print()
for r1 in range(q1, 0, -1):
    for a1 in range(r1, q1 - 1):
        print(' ', end=' ')
    for t1 in range(0, r1):
        print('*', end=' ')
    print()

# Равносторонний треугольник

s = int(input('Введите число: '))
d = 2 * s - 2
for m in range(0, s):
    for j in range(0, d):
        print(end=' ')
    d = d - 1
    for f in range(0, m + 1):
        print('*', end=' ')
    print(' ')

# Его можно и другим, более простым способом вывести, используя формулу:

hg2 = int(input('Введите число: '))
for ng2 in range(hg2, 0, -1):
    print(' ' * ng2 + '*' * (hg2 - ng2 * 2) + ' ' * ng2)

# Перевёрнутый равносторонний треугольник

s2 = int(input('Введите число: '))
d2 = 2 * s2 - 2
for m2 in range(s2, -1, -1):
    for j2 in range(d2, 0, -1):
        print(end=' ')
    d2 = d2 + 1
    for j in range(0, m2 + 1):
        print('*', end=' ')
    print('')

# Также более простым способом вывести, используя формулу:

hg = int(input('Введите число: '))
for ng in range(0, hg):
    print(' ' * ng + '*' * (hg - ng * 2) + ' ' * ng)
