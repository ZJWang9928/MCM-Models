"""
    _               _            _ 
   / \   _ __  _ __(_) ___  _ __(_)
  / _ \ | '_ \| '__| |/ _ \| '__| |
 / ___ \| |_) | |  | | (_) | |  | |
/_/   \_\ .__/|_|  |_|\___/|_|  |_|
        |_|                        

@author: Jonathan Wang
@coding: utf-8
@environment: Manjaro 18.1.5 Juhraya
@date: 16th Jan., 2020

"""

def fakeDataset():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataset):
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return C1

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in map(frozenset, Ck):
            if can.issubset(tid):
                if not can in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1

    numItems = float(len(D))
    retList  = []
    supportData = {}

    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[: k-2]
            L2 = list(Lk[j])[: k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList

def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1];k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)

        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        if len(Lk) == 0:
            break
        L.append(Lk)
        k += 1
    return L, supportData


if __name__ == '__main__':
    dataset = fakeDataset()
    print('Dataset: ', dataset)

    L1, supportData1 = apriori(dataset, minSupport=0.7)
    print()
    print ('L(0.7): ', L1)
    print ('supportData(0.7): ', supportData1)

    L2, supportData2 = apriori(dataset, minSupport=0.5)
    print()
    print ('L(0.5): ', L2)
    print ('supportData(0.5): ', supportData2)

    L3, supportData3 = apriori(dataset, minSupport=0.1)
    print()
    print ('L(0.1): ', L3)
    print ('supportData(0.1): ', supportData3)


