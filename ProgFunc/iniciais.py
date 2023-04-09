# Função que capitaliza as iniciais
def capitaliza_iniciais(frase):
    # Divide a frase em palavras, cada palavra fica com a inicial maiuscula
    # O join junta as palavras novamente em uma frase só e com um espaço entre cada palavra
    return ' '.join(map(str.capitalize, frase.split()))

# Frase que será capitalizada
frase = "tenho que deixar todas as iniciais maiusculas"

# Mostra a frase já capitalizada
print(capitaliza_iniciais(frase))