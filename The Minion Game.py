def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    userc = 'Stuart'
    scorec = 0
    userv = 'Kevin'
    scorev = 0
    for i in range(len(string)):
        if string[i] in vowels:
            scorev += len(string) - i
        else:
            scorec += len(string) - i
    if scorev > scorec:
        print(userv,scorev)
    elif scorev < scorec:
        print(userc,scorec)
    else:
        print('Draw')

