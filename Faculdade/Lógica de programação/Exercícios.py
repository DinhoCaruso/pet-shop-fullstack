#def contagem_progressiva (n):
#    for i in range (1, n+1, 1):   #
#        print(i)

#def contagem_regressiva(n):
#    for i in range (n, 0, -1):
#        print(i)

#x = int(input('x? '))
#opcao = input('Opção? ')
#if opcao in 'Pp':
#    contagem_progressiva(x)
#else:
#    contagem_regressiva(x)

#x = [39, 25, 72, 80, 15, 50, 44, 50]
#x[0] = 88
#print (x[0])

#def encontra_indices(v, s):
#    indices = []
#    for i, item in enumerate(s):
#        if item == v:
#            indices.append(i)

#    return indices


#import copy
#L1 = [10, 20, 30, [40, 50], 60]
#L2 = L1
#L3 = copy.copy(L1)
#L4 = L1[:]
#L5 = L1.copy()
#L6 = list(L1)
#L7 = copy.deepcopy(L1)


#print (L7)


# M = [[68, 86, 50, 42, 84, 98, 75],
#     [15, 83, 10, 16, 14, 99, 58],
#     [30, 68, 78, 44, 70, 25, 31],
#     [69, 53, 17, 87, 55, 83, 15],
#     [20, 70, 78, 61, 65, 16, 26]]


#def soma_nucleo(M, L, C):
#    soma = 0
#    for i in range(1, L):
#        for j in range(1, C):
#            soma += M[i][j]
#    return soma
