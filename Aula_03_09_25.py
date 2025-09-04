# Function remove_smallest() CodeWars
import os

def minhaFuncao(lista):
    if len(lista) == 0:
        return []
    
    minimoLista = min(lista)
    listaBackup = lista.copy()

    for i in listaBackup:

        if i == minimoLista:

            listaBackup.remove(i)
            return f"Lista original: {lista}; Lista Final: {listaBackup}."
        
def minhaFuncaoSolucaoSala(lista):
    if len(lista) == 0:
        return []

    m = min(lista)

    nova = []

    for i in lista:
        nova.append(i)
    
    # Ou 
    # nova = [i for i in lista]

    nova.remove(m)
 
    return f"Lista original: {lista}; Lista Final: {nova}."

print(minhaFuncao([2,4,5,8]))
print(minhaFuncao([2,4,5,2,8]))
print(minhaFuncao([]))

os.system('pause')
os.system('cls')

print(minhaFuncaoSolucaoSala([2,4,5,8]))
print(minhaFuncaoSolucaoSala([2,4,5,2,8]))
print(minhaFuncaoSolucaoSala([]))


os.system('pause')
os.system('cls')

# Function position() CodeWars

def minhaFuncaoPosition(x, y, n):

    hebert = sum(range(x))

    primeiroNumero = (y - hebert) // x

    sequencia = list(range(primeiroNumero, primeiroNumero + x))

    return f"Para uma lista com {x} itens, na qual sua soma é {y}, retorne o item da posição {n}.\n\
    A sequência é {sequencia} e o número {sequencia[n]}."

def solucaoSalaPosition(x, y, n):

    numeroMeioSequencia = y // x
    posicaoNumeroMeio = x // 2

    lista = []
    impar = 0

    if x % 2 == 1:
        lista.append(numeroMeioSequencia)
        impar = 1

    for i in range(posicaoNumeroMeio):
        lista.insert(0, numeroMeioSequencia - impar - i)

    for i in range(posicaoNumeroMeio):
        lista.append(numeroMeioSequencia + i + 1)

    return f"Para uma lista com {x} itens, na qual sua soma é {y}, retorne o item da posição {n}.\n\
    A sequência é {lista} e o número {lista[n]}."

print(minhaFuncaoPosition(4, 14, 0))
print(minhaFuncaoPosition(3, 6, 1))
print(minhaFuncaoPosition(4, 46, 2))
print(minhaFuncaoPosition(3, 63, 1))
print(minhaFuncaoPosition(5, 0, 3))
print(minhaFuncaoPosition(4, -14, 0))
print(minhaFuncaoPosition(4, -2, 2))

os.system('pause')
os.system('cls')

print(solucaoSalaPosition(4, 14, 0))
print(solucaoSalaPosition(3, 6, 1))
print(solucaoSalaPosition(4, 46, 2))
print(solucaoSalaPosition(3, 63, 1))
print(solucaoSalaPosition(5, 0, 3))
print(solucaoSalaPosition(4, -14, 0))
print(solucaoSalaPosition(4, -2, 2))

os.system('pause')
os.system('cls')

# Function accum() CodeWars:

def minhaFuncaoAccum(string):
    novaStr = ""
    for i, letra in enumerate(string):
        novaStr += ((i + 1) * letra).capitalize() + "-"
    
    return novaStr[:-1]

print(minhaFuncaoAccum("abcd"))
print(minhaFuncaoAccum("RqaEzty"))
print(minhaFuncaoAccum("cwAt"))