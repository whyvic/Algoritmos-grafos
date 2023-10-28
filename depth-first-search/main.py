# main.py
from imprime import imprime
from loadlista import loadlista
from dfs import DFS, DFS_visit

[lista_adj, N] = loadlista()

graus_saida = [len(lista_adj[u]) for u in range(N)]
vertice_maior_saida = graus_saida.index(max(graus_saida))
V = [vertice_maior_saida] + [u for u in range(N) if u != vertice_maior_saida]

cor = ["Branco"] * N
d = [0] * N
f = [0] * N
mark = 0
mark = DFS(V, cor, lista_adj, d, f, mark)
imprime(d, f, N)

