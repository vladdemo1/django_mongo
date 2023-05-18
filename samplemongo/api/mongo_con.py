from pymongo import MongoClient

from .con.key import MONGO_PASS


CON_STR = f'mongodb+srv://vladdemo:{MONGO_PASS}@demchenko.2pybcro.mongodb.net/'


def get_client():
        return MongoClient(CON_STR)
