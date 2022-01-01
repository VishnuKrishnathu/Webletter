from pymongo import MongoClient
import environ  # importing django-environ to read env files

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# uri string
URI_STRING= 'mongodb+srv://{username}:{password}@cluster0.ragko.mongodb.net/{database}?retryWrites=true&w=majority'.format(
    username= env('MONGO_USERNAME'),
    password= env('MONGO_PASSWORD'),
    database= env('MONGO_DATABASE')
)
client = pymongo.MongoClient(URI_STRING)

db = client['webletter']