cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    s = [0,1]
    for i in range(2,n):
        s.append(s[i - 2] + s[i - 1])
    return s

