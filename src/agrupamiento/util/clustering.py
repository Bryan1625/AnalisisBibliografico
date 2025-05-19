from scipy.cluster.hierarchy import linkage

def clustering_ward(matrix):
    return linkage(matrix.toarray(), method='ward')

def clustering_average(matrix):
    return linkage(matrix.toarray(), method='average')
