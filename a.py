import numpy as np

def avg(a):
    c = 0
    n = 0
    for x in a:
        c+=1
        n+=int(x)
    res = n/c
    print(res)

def med(n):
    sorted(n)
    c = 0
    for x in n:
        c += 1
    if c%2 == 0:
        z1 = int(n[int(c/2)-1])
        z2 = int(n[int(c/2)])
        res = (z1+ z2)/2
        print(f"med: {res}")
    else:
        res = n[int((c/2))]
        print(f'med: {res}')
    
def mode_(n):
    val, count = np.unique(n, return_counts=True)
    xx1 = []
    for x in val:
        xx1.append(int(x))
    xx2 = []
    for x in count:
        xx2.append(x)
    print(f' {xx1}\n {xx2}')


mode = 'PS'
while True:
    cmd_r = str(input(f'= {mode} > '))
    cmd_r = cmd_r.lower()
    cmd = cmd_r.split(' ')
    print(cmd)
    if mode == 'PS':
        if cmd[0] == 'avg':
            if len(cmd) > 1:
                cmd.remove('avg')
                print(cmd)
                avg(cmd)
            elif len(cmd) == 1:
                mode = "AVG"
        elif cmd[0] == 'med':
            if len(cmd) > 1:
                cmd.remove('med')
                med(cmd)
            elif len(cmd) == 1:
                mode = "MED"
        elif cmd[0] == 'mode':
            if len(cmd) > 1:
                cmd.remove('mode')
                mode_(cmd)
            elif len(cmd) == 1:
                mode = "MODE"