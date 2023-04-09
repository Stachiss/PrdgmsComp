cor(azul).
cor(vermelho).
cor(verde).

aresta(a, b).
aresta(a, c).
aresta(a, d).
aresta(b, c).
aresta(c, d).
aresta(d, a).

coloracao(Grafo, Coloracao) :-
    length(Grafo, N),
    length(Coloracao, N),
    colorir(Grafo, Coloracao).

colorir([], _).
colorir([Vertice|RestoGrafo], Coloracao) :-
    member(Vertice-Cor, Coloracao),
    cor(Cor),
    \+ (member(Vertice2-Cor2, Coloracao), adjacente(Vertice, Vertice2), Cor == Cor2),
    colorir(RestoGrafo, Coloracao).

adjacente(A, B) :- aresta(A, B).
adjacente(A, B) :- aresta(B, A).

% Possível Consulta: coloracao([a,b,c,d], Coloracao).