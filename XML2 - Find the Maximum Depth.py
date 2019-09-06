

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if maxdepth < level + 1:
        maxdepth = level + 1
    for e in list(elem):
        depth(e,level + 1)

