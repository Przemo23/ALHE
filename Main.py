import os
import shelve
import TokenClass
import pprint
import operator
import Algorithm


def fillDiscipline(shelf):
    global disciplinesTokens
    tokens = []
    file = shelve.open(shelf)
    A = file['A']
    P = file['P']
    u = file['u']
    w = file['w']
    udzial = file['udzial']
    publicationIds = file['publicationIdList']
    authorIds = file['authorIdList']
    for i in range(A):
        if file['pracownik'][i] != 1:
            continue
        for j in range(P):
            if u[i][j] != 0:
                tokens.append(TokenClass.Token(authorIds[i],
                                               publicationIds[j],
                                               udzial[i],
                                               u[i][j],
                                               w[i][j]))
    disciplinesTokens[shelf] = tokens
    file.close()


#############################
#         MAIN  CODE        #
#############################
os.chdir(r'.\Resources')

shelvesNames = []
disciplinesTokens = {}

'''for fileName in os.listdir(os.getcwd()):
    if fileName.endswith(".dat"):
        shelvesNames.append(fileName[0:-4])

for shelf in shelvesNames:
    TokenClass.Token.tokenIndex = 1
    fillDiscipline(shelf)'''

dataShelve = shelve.open('sorted')
disciplinesTokens = dataShelve['disciplinesTokens']
dataShelve.close()

for discipline in disciplinesTokens:
    print("Result in "+ discipline)
    for i in range(0,26):
        print(Algorithm.Alg(disciplinesTokens[discipline]))




