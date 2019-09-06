def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string) // k):
        l = list(string[i * k:(i + 1) * k])
        nl = []
        for c in l:
            if not c in nl:
                nl.append(c)
        print(''.join(nl))

