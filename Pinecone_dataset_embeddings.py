import pinecone      
import openai
import pandas as pd

pinecone.init(      
	api_key='9e27e17a-bdfe-4f14-9e0f-e7e581695e39',      
	environment='gcp-starter'      
)      

openai.api_key = "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"

def create_embedding(input_text):
    response = openai.Embedding.create(
        input=input_text,
        model="text-embedding-ada-002"
    )
    embedding = response['data'][0]['embedding']
    return embedding

# Cargar el archivo CSV en un DataFrame
dataframe = pd.read_csv('c:\\Users\\Br1\\Desktop\\dataset_chatbot.csv')

# Convertir el DataFrame en un diccionario
data_dict = dataframe.set_index('id').to_dict('index')
print("Datos cargados")

vectors = [(key, create_embedding(value['informacion']), {"metadata": value['metadata'], "value": value['value']}) for key, value in data_dict.items()]
print("EMBEDDING REALIZADO CON EXITO: "+str(len(vectors))+" vectores creados")
# Borra el índice existente
try :
    pinecone.delete_index("ltiuy")
    print("Index ltiuy antiguo borrado con exito")
except :
    print("No hay indices para borrar")

# Crea un nuevo índice
pinecone.create_index("ltiuy", metric="cosine", index_type="text", dimension=1536)
print("Nuevo index ltiuy creado con exito")

index = pinecone.Index('ltiuy')

upsert_response = index.upsert(vectors)
print("Embeddings cargados con exito en Pinecone")