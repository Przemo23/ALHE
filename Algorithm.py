import random


class Params:

    disciplineVal = 0
    disciplineLim = 0
    toDraw = []
    workerLims = {}
    workerVals = {}

    def __init__(self,disciplineTokens):

        for token in disciplineTokens:
            self.workerLims[token.authorID] = 4 * float(token.participation)
            self.workerVals[token.authorID] = 0
        for workerLim in self.workerLims:
            self.disciplineLim += float(self.workerLims[workerLim]) * 3 / 4
        self.zeroPlacement = len(disciplineTokens) - 1
        self.disciplineList = CreatePermutations(disciplineTokens)
        self.toDraw = list(range(0,len(disciplineTokens)))

def Alg(disciplineTokens):

    params = Params(disciplineTokens)

    for i in range(0,100000):
        a = random.choice(params.toDraw)
        if a == params.zeroPlacement:
            continue
        Operation(a,disciplineTokens,params)

    result = 0
    for tokens in params.toDraw:
        if CheckIfPossibleToAdd(tokens,disciplineTokens,params):
            Swap(a, params.disciplineList, params)

    for i in range(1,len(disciplineTokens)):
        if params.disciplineList[i] == i:
            result += disciplineTokens[i-1].value


    return result

def CreatePermutations(disciplineTokens):
    disciplineList = []
    disciplineList = (list(range(1, len(disciplineTokens))))
    disciplineList.append(0)
    return disciplineList

def Operation(a,disciplineTokens,params):
    if CheckIfPossibleToAdd(a,disciplineTokens,params):
        params.toDraw.remove(params.disciplineList[a])
        Swap(a,params.disciplineList,params)


def Swap(a,disciplineList,params):
    temp = disciplineList[disciplineList[a]]
    disciplineList[disciplineList[a]] = disciplineList[a]
    disciplineList[a] = temp
    if disciplineList[a] == a:
        disciplineList[params.zeroPlacement] = disciplineList[a]
        disciplineList[a] = 0
        params.zeroPlacement = a


def CheckIfPossibleToAdd(a,disciplineTokens,params):
    if disciplineTokens[a].pubParticipation + params.disciplineVal <= params.disciplineLim and disciplineTokens[a].pubParticipation + params.workerVals[disciplineTokens[a].authorID] <= params.workerLims[disciplineTokens[a].authorID]:
        params.workerVals[disciplineTokens[a].authorID] += disciplineTokens[a].pubParticipation
        params.disciplineVal += disciplineTokens[a].pubParticipation
        return True
    return False

