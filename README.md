graph
=====

Autora: Camila Maia - matrícula: 11201012

Software produzido na disciplina Grafos, INE5413, do departamento de Informática e Estatística da Universidade Federal de Santa Catariana.

=====

Este script calcula a menor distância entre dois nodos dado um grafo, utilizando o algoritmo de Dijkstra.

Para executar o arquivo, entre no diretório do projeto e execute o comando ./bin/graph

ex: ~/workspace/graph$ ./bin/graph

Existem dois argumentos opcionais:

  -h, --help  mostra um texto de ajuda
  -c          permite criar seu próprio grafo.

Por padrão o script calcula a menor distância entre dois pontos aleatórios para este determinado grafo (que foi estudado em sala de aula):

  {
     A {'B': 7, 'G': 3, 'F': 5}
     C {'B': 2, 'E': 3, 'D': 5, 'G': 2}
     B {'A': 7, 'C': 2, 'G': 3}
     E {'C': 3, 'D': 4, 'G': 4, 'F': 6}
     D {'C': 5, 'E': 4}
     G {'A': 3, 'C': 2, 'B': 3, 'E': 4, 'F': 3}
     F {'A': 5, 'E': 6, 'G': 3}
  }