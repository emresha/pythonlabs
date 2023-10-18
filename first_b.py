def main(givenList, k, element):
    newList = givenList.copy()
    newList.append(None)
    previousElement = newList[k]
    for i in range(len(newList) - 1, k, -1):
        newList[i], newList[i - 1] = newList[i - 1], newList[i]
    newList[k] = element
    return newList
