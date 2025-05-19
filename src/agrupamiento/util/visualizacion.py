import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def graficar_dendrograma(linkage_matrix, titulos, metodo):
    plt.figure(figsize=(12, 6))
    dendrogram(linkage_matrix, labels=titulos, leaf_rotation=90)
    plt.title(f'Dendrograma - Método: {metodo}')
    plt.tight_layout()
    plt.show()
