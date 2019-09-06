if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    #l.sort(key=lambda x:x[1])
    nl = list(set(map(lambda l:l[1],l)))
    nl.sort()
    score2 = nl[1]
    #print(score2)
    names = []
    for o in l:
        if o[1] == score2:
            names.append(o[0])
    #print(names)
    names.sort()
    #print(names)
    for n in names:
        print(n)



