import numpy as np

def avg(a):
    try:
        c = 0
        n = 0
        for x in a:
            c+=1
            n+=int(x)
        res = n/c
        print(res)
    except:
        print(f'??? pls use [int]')

def med(n):
    try:
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
    except:
        print(f'??? pls use [int]')
    
def mode_(n):
    try:
        val, count = np.unique(n, return_counts=True)
        xx1 = []
        for x in val:
            xx1.append(int(x))
        xx2 = []
        for x in count:
            xx2.append(x)
        print(f' {xx1}\n {xx2}')
    except:
        print(f'??? pls use [int]')


mode = 'PS'
while True:
    cmd_r = str(input(f'= {mode} > '))
    cmd_r = cmd_r.lower()
    cmd = cmd_r.split(' ')
    if mode == 'PS':
        if cmd[0] == 'avg':
            if len(cmd) > 2:
                cmd.remove('avg')
                print(cmd)
                avg(cmd)
            elif len(cmd) > 1 and len(cmd) < 2:
                print('wfs pls avg x1 x2 x3 not x1')
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
                cmd.remove('mo')
                mode_(cmd)
            elif len(cmd) == 1:
                mode = "MO"
        elif cmd[0] == 'help':
            print('avg [int, int, ..., int] to average')
            print('med [int, int, ..., int] to median')
            print('mo [int, int, ..., int] to mode')
            print('    - by RIZC using numpy -    \n github: https://github.com/RINZC')
        else:
            print ("Unknown command: %s" % cmd[0])
            print ("help to show command ")
    if mode == 'AVG':
        try:
            if len(cmd) != 0:
                avg(cmd)
        except:
            print('this mode only n1, n2, n3, ..., nx')