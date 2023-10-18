def main(givenList, k):
    count = 0
    for i in range(1, len(givenList) - 1):
        if givenList[i - 1] < givenList[i] and givenList[i] > givenList[i + 1] or\
                givenList[i - 1] > givenList[i] and givenList[i] < givenList[i + 1]:
            count += 1
        if count == k:
            return givenList[i]
    return None
