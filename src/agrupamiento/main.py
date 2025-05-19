import pandas as pd
from src.agrupamiento.util import preprocesamiento, similitud, clustering, visualizacion, evaluacion

def main():
    # Cargar y limpiar datos
    df = pd.read_csv('C:/Users/Bryan/Documents/btw/code/Programacion/ProyectoAlgoritmos/src/agrupamiento/data/abstracts.csv')
    df.dropna(subset=['contenido', 'titulo', 'categoria'], inplace=True)
    df['texto_limpio'] = df['contenido'].apply(preprocesamiento.preprocesar_texto)

    # Vectorizar
    X = similitud.vectorizar_textos(df['texto_limpio'])

    # Clustering
    ward = clustering.clustering_ward(X)
    average = clustering.clustering_average(X)

    # Graficar dendrogramas
    visualizacion.graficar_dendrograma(ward, df['titulo'].tolist(), metodo='ward')
    visualizacion.graficar_dendrograma(average, df['titulo'].tolist(), metodo='average')

    # Evaluar coherencia con categorías reales
    etiquetas_reales = df['categoria'].factorize()[0]
    n_clusters = df['categoria'].nunique()
    ari_ward = evaluacion.evaluar_clustering(ward, etiquetas_reales, n_clusters)
    ari_avg = evaluacion.evaluar_clustering(average, etiquetas_reales, n_clusters)

    print(f"Índice de Rand Ajustado (Ward): {ari_ward:.2f}")
    print(f"Índice de Rand Ajustado (Average): {ari_avg:.2f}")

if __name__ == '__main__':
    main()
