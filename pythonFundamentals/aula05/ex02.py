def minimo(lista):
    minimo = lista[0]
    for num in lista[1:]:
        if num < minimo:
            minimo = num
    return minimo

def maximo(lista):
    maximo = lista[0]
    for num in lista[1:]:
        if num > maximo:
            maximo = num
    return maximo

def menorValorPar(lista):
    lista_par = []
    for numero in lista:
        if numero%2 == 0:
            lista_par.append(numero)
    return minimo(lista_par)

def maiorValorImpar(lista):
    lista_impar = []
    for numero in lista:
        if numero%2 == 1:
            lista_impar.append(numero)

    return maximo(lista_impar)


def main():
    lista = [1, 3, 4, 10, 54]
    menor_valor = minimo(lista)
    maior_valor = maximo(lista)
    menor_valor_par = menorValorPar(lista)
    maior_valor_impar = maiorValorImpar(lista)
    print(f"Menor valor da lista: {menor_valor}")
    print(f"Maior valor da lista: {maior_valor}")
    print(f"Menor valor par da lista: {menor_valor_par}")
    print(f"Maior valor impar da lista: {maior_valor_impar}")

if __name__ == "__main__":
    main()    