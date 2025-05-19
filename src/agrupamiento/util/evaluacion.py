from sklearn.metrics import adjusted_rand_score
from scipy.cluster.hierarchy import fcluster

def evaluar_clustering(linkage_matrix, categorias_reales, n_clusters):
    predicciones = fcluster(linkage_matrix, n_clusters, criterion='maxclust')
    return adjusted_rand_score(categorias_reales, predicciones)
