# Importa a função reduce da biblioteca functools
from functools import reduce

# Define uma lista de coeficientes de um polinômio
# Ex: 2x^0 - 3x^1 + 0x^2 + 5x^3
polinomio = [2, -3, 0, 5]

# Define uma função que calcula o valor do polinômio em um ponto específico
def calcular_polinomio(coeficientes, x=0):
    # Define uma função lambda que calcula o valor de um termo do polinômio
    calcular_termo = lambda coeficiente, expoente, x: coeficiente * (x ** expoente)

    # Usa a função map para aplicar a função lambda a cada par (coeficiente, expoente) da lista de coeficientes
    # e obter uma lista de termos do polinômio
    termos = list(map(calcular_termo, coeficientes, range(len(coeficientes)), [x]*len(coeficientes)))
    # Usa a função reduce para somar os termos e obter o valor final do polinômio
    return reduce(lambda a, b: a + b, termos)

# Calcula o valor do polinômio no ponto x=2
valor = calcular_polinomio(polinomio, 2)

# Imprime o valor calculado
print(valor)