def swap_case(s):
    d = {}
    for i in range(26):
        d[chr(ord('A') + i)] = chr(ord('a') + i)
        d[chr(ord('a') + i)] = chr(ord('A') + i)
    #print(d)
    return s.translate(str.maketrans(d))

