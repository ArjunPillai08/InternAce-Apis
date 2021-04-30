import pymongo, ssl, os
from dotenv import load_dotenv
load_dotenv()

def connect_to_db():
    ssl._create_default_https_context = ssl._create_unverified_context
    client = pymongo.MongoClient(os.environ['MONGO_CONNECTION_STRING'], ssl_cert_reqs=ssl.CERT_NONE)
    db = client['InternAce']
    collection = db['internships']
    return collection