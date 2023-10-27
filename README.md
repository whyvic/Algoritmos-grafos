# Algoritmos em Grafos

##Implementação do trabalho de algoritmos em grafos

# Algoritmos em Grafos

## Implementação do Trabalho de Algoritmos em Grafos

O trabalho consiste na implementação do algoritmo DFS (Depth-First Search ou busca em profundidade), que é utilizado para percorrer estruturas de dados em forma de grafo. O funcionamento do DFS é relativamente simples:

1. Inicialização: Um nó inicial é escolhido com base em alguma heurística. No nosso trabalho, a heurística escolhida é o vértice com o maior grau de saída, que será o vértice/nó inicial.

2. Exploração: A partir desse vértice inicial, escolhemos um dos seus vizinhos, ou seja, vértices que pertencem à lista de adjacência do vértice inicial, e verificamos se ele está na cor "branca". Se estiver na cor "branca", ele é marcado como "cinza" e a função DFS é chamada recursivamente para explorar esse vértice e seus vizinhos. Esse processo continua até que não haja mais vértices "brancos" a serem explorados, quando isso acontece o vertice é marcado como "preto.

3. Backtracking: Quando chegamos a um vértice que não possui mais nenhum vizinho "branco" a ser explorado, fazemos o "backtracking", ou seja, retornamos até o último ponto onde existem vizinhos "brancos" a serem explorados. Esse processo continua até que toda a árvore esteja completamente explorada e todos os vértices estejam marcados como "preto".

O DFS é uma técnica importante para percorrer grafos e encontrar informações relevantes. Ele é amplamente utilizado em algoritmos de busca e análise de conectividade em grafos.

