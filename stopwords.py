# importar la libreria nltk
import nltk
# desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
lista_stopwords = stopwords.words('spanish')
#imprimir las stopwords
print(lista_stopwords)


# Importar Libreria nltk
import nltk

from nltk.corpus import stopwords
nltk.download('stopwords')

# definir la ruta donde se encuentra los datos descargados de nltk
nltk.data.path.append('C:/Users/Leonardo_Duarte/AppData/Roaming/nltk_data')

# Importar la librería NLTK 
import nltk 

# Desde NLTK, importamos las stopwords que son las palabras comunes en un idioma
from nltk.corpus import stopwords

# Descargamos la lista de palabras vacías stopwords sino está disponible en nuestra computadora
nltk.download('stopwords')

# Guardar en una variable la lista de stopwords en español
lista_de_stopwords = stopwords.words('spanish')

# Imprimir la lista de stopwords
print(lista_de_stopwords)








