from flask import Flask, request
from flask_cors import cross_origin
from utils import pdf, embeddings
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_huggingface.llms import HuggingFaceEndpoint
import pandas


categories = pandas.read_csv('server-python/data/desafio_tecnico_ai_eng - categories.csv')
costumers = pandas.read_csv('server-python/data/desafio_tecnico_ai_eng - costumers.csv')
order_items = pandas.read_csv('server-python/data/desafio_tecnico_ai_eng - order_items.csv')
orders = pandas.read_csv('server-python/data/desafio_tecnico_ai_eng - orders.csv')
products = pandas.read_csv('server-python/data/desafio_tecnico_ai_eng - products.csv')
promotions = pandas.read_csv('server-python/data/desafio_tecnico_ai_eng - promotions.csv')

politica = pdf.process_file('server-python/data/políticas_da_loja.pdf')

function_embedding = HuggingFaceEmbeddings()

db = Chroma(persist_directory="database", embedding_function=function_embedding)

result = db.similarity_search_with_relevance_scores("question", k=5)

response = result[0]

app = Flask(__name__)

@app.route("/", methods=["POST"])
@cross_origin()
def send_question():
    text = request.json["text"]

    

    return []