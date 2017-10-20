from timeit import default_timer
from math import sqrt
start = default_timer()

allPrimes = [2, 3, 5]
modPrimes = set({1, 5})
modExtras = set({})
loopPrimes = list([5])
modPrimesIndex = 1
modComposite = 6

def isPrime(testNum, loopPrimes):
    for factor in loopPrimes:
        if factor > sqrt(testNum):
            return True
        if testNum % factor == 0:
            return False

def getExtras(modPrimes, modPrimesIndex, modComposite, allPrimes):
    minIndex = modPrimesIndex + 2
    maxIndex = modPrimesIndex + 2
    while (allPrimes[minIndex] * allPrimes[maxIndex] < modComposite):
        modPrimes |= set({allPrimes[minIndex] * allPrimes[maxIndex]})
        maxIndex += 1
    for i in range(minIndex, maxIndex - 1):
        findExtra(i, allPrimes[i], modPrimes, allPrimes, modComposite)
    return

def findExtra(i, num, modPrimes, allPrimes, modComposite):
    j = 0
    while (num * allPrimes[i + j] < modComposite):
        modPrimes |= {num * allPrimes[i + j]}
        findExtra(i, num * allPrimes[i + j], modPrimes, allPrimes, modComposite)
        j += 1
    return

for testNum in range(7, 10000000):
    if testNum % 1000000 == 0: ##just a helpful output to see where the program is
        end = default_timer()
        print '{} in {} seconds'.format(testNum, end - start)

    if testNum == modComposite * allPrimes[modPrimesIndex + 1]:
        modComposite *= allPrimes[modPrimesIndex + 1]
        modPrimes -= modExtras
        modExtras.clear()
        modPrimes.remove(allPrimes[modPrimesIndex + 1])
        loopPrimes.remove(allPrimes[modPrimesIndex + 1])
        modPrimes |= set(loopPrimes)
        getExtras(modExtras, modPrimesIndex, modComposite, allPrimes) ##need to add to modPrimes numbers composed of primes greater than modPrimesIndex + 1
        modPrimes |= modExtras
        modPrimesIndex += 1
    element = testNum % modComposite
    if element in modPrimes:
        if isPrime(testNum, loopPrimes):
            allPrimes.append(testNum)
            loopPrimes.append(testNum)
end = default_timer()
# print allPrimes
print('{} numbers were found in {} seconds'.format(len(allPrimes), end - start))
