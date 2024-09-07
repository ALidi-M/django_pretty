from pymongo import MongoClient

# MongoDB settings
# MONGO_DB_NAME = 'Sampledb'
MONGO_DB_NAME = 'sample_airbnb'
MONGO_HOST = 'mongodb+srv://ahmadmponda:ipass.com@cluster0.a8umg.mongodb.net'
MONGO_OPTIONS = '?retryWrites=true&w=majority&appName=Cluster0'

# Connection URI
MONGO_URI = f'{MONGO_HOST}{MONGO_OPTIONS}'

# Create MongoDB client
mongo_client = MongoClient(MONGO_URI)

# Access the database
mongo_db = mongo_client[MONGO_DB_NAME]
