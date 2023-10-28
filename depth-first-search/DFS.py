def DFS_visit(u, cor, d, f, lista_adj, mark):
    cor[u] = "Cinza"
    mark = mark + 1
    d[u] = mark
    for v in lista_adj[u]:
        if cor[v] == "Branco":
            print("Aresta", u+1, "-", v+1, ": Arvore")
            mark = DFS_visit(v, cor, d, f, lista_adj, mark)
        elif cor[v] == "Cinza":
            print("Aresta", u+1, "-", v+1, ": Retorno")
        elif cor[v] == "Preto" and d[u] < d[v]:
            print("Aresta", u+1, "-", v+1, ": Avanco")
        else:
            print("Aresta", u+1, "-", v+1, ": Cruzamento")
    cor[u] = "Preto"
    mark = mark + 1
    f[u] = mark
    return mark

def DFS(V, cor, lista_adj, d, f, mark):
    for u in V:
        cor[u] = "Branco"
    for u in V:
        if cor[u] == "Branco":
            mark = DFS_visit(u, cor, d, f, lista_adj, mark)
    return mark
