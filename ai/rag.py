# Dependencies
import os
import json
import datetime
import joblib as jbl
from langchain_milvus import Milvus
from utils.auth import load_credentials
from huggingface_hub import InferenceClient
from pymilvus import connections, Collection, FieldSchema, DataType, CollectionSchema


# A class for managing embeddings and retrieval
class RAG:
    def __init__(self):
        self.hf_token, self.model = load_credentials('embeddings')
        self.hf_client = InferenceClient(token = self.hf_token, model = self.model)
        self.milvus_uri, self.milvus_token = load_credentials('milvus')
        self.connect_to_milvus = connections.connect(alias = 'default', uri = self.milvus_uri, token = self.milvus_token)
        self.data = self.load_data()
        self.collection_name = 'xplendid_collection'


    # A utility function to load the dataset
    def load_data(self):
        data = []
        with open('data/qa_dataset.jsonl', 'r', encoding = 'utf-8') as f:
            for line in f:
                data.append(json.loads(line))
        return data


    # A function for getting embeddings
    def get_embeddings(self):
        embeddings_path = 'data/qa_embeddings.joblib'
        embeddings_ctime = os.path.getctime(embeddings_path)
        last_update = datetime.datetime.fromtimestamp(embeddings_ctime).date()
        today = datetime.datetime.today().date()
        data = self.data
        
        if ((today > last_update) and (today.day == 7)) or (not os.path.exists(embeddings_path)):
            # Initializing the inference client and getting embeddings
            client = self.hf_client
            embeddings = [
                client.feature_extraction(text = item['answer'])
                for item in data
                ]
            jbl.dump(embeddings, embeddings_path)
        else:
            embeddings = jbl.load(embeddings_path)
        return embeddings


    # A function to get the embedding for a query
    def embed_query(self, text: str):
        return self.hf_client.feature_extraction(text = text)
    

    # A function to get embeddings for documents
    def embed_documents(self, texts: list[str]):
        return [self.hf_client.feature_extraction(text=t) for t in texts]
        

    # A function to load the collection into Milvus
    def load_collection(self):
        # Getting embeddings and data
        embeddings = self.get_embeddings()
        data = self.data

        # Connecting to Milvus
        self.connect_to_milvus

        # Setting up the collection schema
        fields = [
        FieldSchema(name = 'id', dtype = DataType.INT64, is_primary = True, auto_id = True),
        FieldSchema(name = 'question', dtype = DataType.VARCHAR, max_length = 512),
        FieldSchema(name = 'answer', dtype = DataType.VARCHAR, max_length = 2048),
        FieldSchema(name = 'embedding', dtype = DataType.FLOAT_VECTOR, dim = 384)
        ]
        schema = CollectionSchema(fields, description = 'xplendid embeddings')
        collection = Collection(self.collection_name, schema = schema)
        questions = [item['question'] for item in data]
        answers = [item['answer'] for item in data]
        collection.insert([questions, answers, embeddings])
        
        # Creating the index
        index_params = {
                'index_type': 'HNSW',
                'metric_type': 'COSINE',
                'params': {'nlist': 128}
                }
        collection.create_index(field_name = 'embedding', index_params = index_params)
        collection.load()


    # A function to get the retriever
    def get_retriever(self):
        # Connecting to Milvus
        self.connect_to_milvus
        collection = Collection(self.collection_name)
        collection.load()
    
        # Initializing the Milvus vector store and retriever
        vectorstore = Milvus(
        collection_name = self.collection_name,
        embedding_function = self,
        connection_args = {'uri': self.milvus_uri, 'token': self.milvus_token},
        vector_field = 'embedding',
        text_field = 'answer'
        )
        retriever = vectorstore.as_retriever(search_type = 'similarity', search_kwargs = {'k': 3})
        return retriever