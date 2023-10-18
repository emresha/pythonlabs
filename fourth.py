def main(givenList):
    def isPrime(n):
        dividers = 0
        for i in range(1, abs(n) + 1):
            if abs(n) % i == 0:
                dividers += 1
        return True if dividers == 2 else False

    r = givenList.copy()
    arrays = []
    for i in range(len(givenList) - 1):
        arr = [r[i]]
        for j in range(i + 1, len(givenList)):
            if isPrime(r[j]) and isPrime(r[j - 1]) and r[j - 1] > r[j]:
                arr.append(r[j])
            else:
                break
        if len(arr) != 1:
            arrays.append(arr)
    r = sorted(arrays, key=len, reverse=True)

    return r[0] if len(r) != 0 else "No sequence found"
