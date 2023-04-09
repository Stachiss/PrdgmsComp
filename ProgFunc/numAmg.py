def soma_divisores(n):
    return sum(filter(lambda i: n % i == 0, map(lambda i: i, range(1, n))))

def eh_amigo(n):
    return list(filter(lambda pair: soma_divisores(pair[0]) == pair[1] and soma_divisores(pair[1]) == pair[0], 
                filter(lambda pair: pair[0] != pair[1], map(lambda i: (i, soma_divisores(i)), range(1, n)))))

print(eh_amigo(10000))
