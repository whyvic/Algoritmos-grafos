def loadlista():
    try:
        arquivo = open('grafos/g6.txt', 'r')
        lista = arquivo.readlines()
        for i in range(len(lista)):
            linha = lista[i].split()
            if i == 0:
                N = int(linha[0])
                lista_adj = [[] for _ in range(N)]
            else:
                lista_adj[int(linha[0])-1].append(int(linha[1])-1)
        arquivo.close()
        return lista_adj, N
    except FileNotFoundError:
        print("O arquivo nao pode ser encontrado. Verifique o caminho do arquivo.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {str(e)}")
        return None, None
