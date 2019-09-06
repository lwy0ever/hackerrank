def print_formatted(number):
    # your code goes here
    #l = len(bin(number).replace('0b',''))
    l = len('{:b}'.format(number))
    s = '{0:' + str(l) + 'd} {0:' + str(l) + 'o} {0:' + str(l) + 'X} {0:' + str(l) + 'b}'
    for i in range(1,number + 1):
        #print(str(i).rjust(l,' '),oct(i).replace('0o','').rjust(l,' '),hex(i).replace('0x','').upper().rjust(l,' '),bin(i).replace('0b','').rjust(l,' '))
        print(s.format(i))

