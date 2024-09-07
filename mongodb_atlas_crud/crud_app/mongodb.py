from pymongo import MongoClient
from dotenv import load_dotenv,find_dotenv
import os
import pprint

load_dotenv(find_dotenv())

password = os.environ.get('MONGODB_PWD')

MONGO_DB_NAME = 'Sampledb'
MONGO_HOST = f"mongodb+srv://ahmadmponda:{password}@cluster0.a8umg.mongodb.net"
MONGO_OPTIONS = '?retryWrites=true&w=majority&appName=Cluster0'

# Connection URI
MONGO_URI = f'{MONGO_HOST}{MONGO_OPTIONS}'

# Creating MongoDB client
mongo_client = MongoClient(MONGO_URI)

# Accessing the database
mongo_db = mongo_client[MONGO_DB_NAME]

