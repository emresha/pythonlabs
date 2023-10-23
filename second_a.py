def main(givenList, k):
    if k >= len(givenList):
        return givenList
    r = givenList.copy()
    del r[k]
    return r

