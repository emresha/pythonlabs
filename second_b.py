def main(givenList, k):
    if k >= len(givenList):
        return givenList
    newList = givenList.copy()
    if k != len(newList) - 1:
        newList[k], newList[k + 1] = newList[k + 1], newList[k]
    else:
        return newList[:k]
    for i in range(k + 1, len(newList) - 1):
        newList[i], newList[i + 1] = newList[i + 1], newList[i]
    return newList[:-1]
