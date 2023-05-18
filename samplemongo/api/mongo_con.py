from pymongo import MongoClient


CON_STR = 'mongodb+srv://vladdemo:postgres@demchenko.2pybcro.mongodb.net/'


def get_client():
        return MongoClient(CON_STR)
