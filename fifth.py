def main(givenList):
    odd = []
    even = []
    for i in range(len(givenList)):
        if givenList[i] % 2 == 0:
            even.append(givenList[i])
        else:
            odd.append(givenList[i])

    fmin = odd[0]
    fmax = even[0]
    for i in even:
        if i < fmin:
            fmin = i
    for i in odd:
        if i < fmax:
            fmax = i

    return fmin, fmax
