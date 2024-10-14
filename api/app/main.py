from pydantic import BaseModel
from fastapi import FastAPI, Body
from typing import Dict, Union, List
from FlagEmbedding import BGEM3FlagModel

app = FastAPI()
model = BGEM3FlagModel('BAAI/bge-m3', use_fp16 = False)

class QueryModel(BaseModel):
    queries: List[str]

@app.post('/m3_embeddings',response_model = Dict[str, Union[
List[List[float]], List[Dict[str, float]], List[List[List[float]]]]])
async def get_m3_embeddings(query_model: QueryModel):
    """
    """
    embeddings = model.encode(
        query_model.queries, batch_size=12, max_length=8192,
        return_dense=True, return_sparse=True, return_colbert_vecs=True)
    
    return {'dense_vecs': embeddings['dense_vecs'],
            'lexical_weights': embeddings['lexical_weights'],
            'colbert_vecs': embeddings ['colbert_vecs']}


