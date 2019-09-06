# Enter your code here. Read input from STDIN. Print output to STDOUT
da,ma,ya = map(int,input().split())
de,me,ye = map(int,input().split())
if ya > ye:
    print(10000)
elif ya == ye and ma > me:
    print((ma - me) * 500)
elif ya == ye and ma == me and da > de:
    print((da - de) * 15)
else:
    print(0)
'''
if ye > ya:
    print(0)
elif ye == ya:
    if me > ma:
        print(0)
    elif me == ma:
        if de >= da:
            print(0)
        else:
            print((da -de)*15)
    else:
        print((ma - me) * 500)
else:
    print(10000)
'''
