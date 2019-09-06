# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    a,b = input().split()
    try:
        print(int(a) // int(b))
    except (ValueError,ZeroDivisionError) as e:
        print('Error Code: %s' % e)
    '''
    except ValueError as e:
        print('Error Code: %s' % e)
    except ZeroDivisionError as e:
        print('Error Code: %s' % e)
    '''
