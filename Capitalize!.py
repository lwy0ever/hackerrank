

# Complete the solve function below.
def solve(s):
    '''
    l = list(s)
    l[0] = l[0].upper()
    for i in range(1,len(l)):
        if l[i - 1] == ' ':
            l[i] = l[i].upper()
    return ''.join(l)
    '''
    return ' '.join(x.capitalize() for x in s.split(' '))

