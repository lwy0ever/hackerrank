if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        c = input().split() + ['']
        #print(c)
        #print('l.%s(%s)' % (c[0],','.join(c[1:])))
        if c[0] == 'print':
            print(l)
        else:
            eval('l.%s(%s)' % (c[0],','.join(c[1:])))
