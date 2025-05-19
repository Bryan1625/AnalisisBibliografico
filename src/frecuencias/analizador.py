import bibtexparser
from collections import Counter
import re

class Analizador:
    def __init__(self, bibtex_path):
        self.abstracts = self._cargar_abstracts(bibtex_path)

    def _cargar_abstracts(self, path):
        with open(path, encoding='utf-8') as f:
            bib = bibtexparser.load(f)
        return [entry.get('abstract', '').lower() for entry in bib.entries]

    def contar_variables(self, categoria):
        contador = Counter()
        for abstract in self.abstracts:
            for grupo in categoria.variables:
                patron = '|'.join([re.escape(pal) for pal in grupo])
                if re.search(r'\b(' + patron + r')\b', abstract):
                    contador[grupo[0]] += len(re.findall(r'\b(' + patron + r')\b', abstract))
        return contador
