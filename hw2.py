import sys
def func():

    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    left = line[0]
    right = line[-1]
    res = list(range(line[0], line[-1] + 1))
    ope = int(input())
    n = len(res)

    for i in range(ope):
        line = sys.stdin.readline().strip()
        line = list(map(int, line.split()))
        o = line[0]
        oo = line[1]
        if o == 1:
            if oo < n:
                res = res[oo:]
                n -= oo
        elif o == 2 and n > 1 and oo >= left and oo <= right:
            try:
                res.remove(oo)
                n -= 1
            except:
                b = 0
        elif o == 3 and oo >= left and oo <= right:
            s = set(res)
            if oo not in res:
                res.append(oo)
                n += 1
    print(res[0])
            

                    
                    
                    
            
            
            
            

if __name__ == "__main__":
    func()
