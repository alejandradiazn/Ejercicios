import numpy as np

candidatos = np.arange(1,31) #pedir hasta 31 por indice 0

#Random: Cada vez que se ejecute  genera resultados que cambian 
#multinomial: pvals ->sequence of floats, length p / probabilidades de cada resultado diferente

votos = np.random.multinomial(5000, np.ones(30)/30)

#Matriz para reunir candidato con su cantidad de votos
resultados = np.column_stack((candidatos, votos))

listaResul = resultados.tolist()

for i in range(len(listaResul)):
    for j in range(i + 1, len(listaResul)):
        if listaResul[i][1] < listaResul[j][1]:
            listaResul[i], listaResul[j] = listaResul[j], listaResul[i]


resultadosOrd = np.array(listaResul)
print("Candidato  Votos")
print("-----------------")
for candidato, voto in resultadosOrd:
    print(f"   {candidato:2d}       {voto:3d}")

