def main(givenList, k):
    newList = []
    for i in range(len(givenList)):
        if i == k:
            pass
        else:
            newList.append(givenList[i])
    return newList
