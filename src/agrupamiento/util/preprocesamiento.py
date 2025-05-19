import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

# Descargar stopwords si no se ha hecho
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocesar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    # Tokenizar
    palabras = texto.split()
    # Eliminar stopwords y aplicar stemming
    palabras_limpias = [stemmer.stem(p) for p in palabras if p not in stop_words]
    # Reconstruir el texto
    return ' '.join(palabras_limpias)

