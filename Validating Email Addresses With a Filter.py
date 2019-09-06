import re

def fun(s):
    # return True if s is a valid email, else return False
    l = re.findall('^([a-zA-Z0-9-_]+)@([a-zA-Z0-9]+)\.([a-zA-Z0-9]{1,3})$',s)
    #print(l)
    if len(l) == 1:
        return True
    else:
        return False

