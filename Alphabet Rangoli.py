def print_rangoli(size):
    # your code goes here
    for i in range(size):
        l = [chr(97 + size - 1 - i)]
        for j in range(i,0,-1):
            l.insert(0,chr(97 + size - j))
            l.append(chr(97 + size - j))
        #print(l)
        print('-'.join(l).center((size - 1) * 4 + 1,'-'))
    for i in range(size - 2,-1,-1):
        l = [chr(97 + size - 1 - i)]
        for j in range(i,0,-1):
            l.insert(0,chr(97 + size - j))
            l.append(chr(97 + size - j))
        #print(l)
        print('-'.join(l).center((size - 1) * 4 + 1,'-'))
