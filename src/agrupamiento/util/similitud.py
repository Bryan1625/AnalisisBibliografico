from sklearn.feature_extraction.text import TfidfVectorizer

def vectorizar_textos(textos):
    #se usa tf-idf term frequency y inverse document frequency
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)
    return X
