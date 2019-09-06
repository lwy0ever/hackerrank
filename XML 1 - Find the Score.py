

def get_attr_number(node):
    # your code goes here
    if len(list(node)) == 0:
        return len(node.attrib)
    s = 0
    for e in list(node):
        s += get_attr_number(e)
    return s + len(node.attrib)


