
def lequal(l1, l2):
    if len(l1) != len(l2):
        return False

    for i in range(len(l1)):
        i = l1[i]
        idx = l2.index(i)
        if idx == -1:
            return False
        l2.remove(i)
    return True