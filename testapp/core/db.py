from pymongo.mongo_client import MongoClient
from django.conf import settings


def get_collection(db_name: str = '', collection: str = ''):

    client = MongoClient(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
    )

    db_handle = client[db_name or settings.DB_NAME]
    return db_handle[collection or settings.TEST_COLLECTION_NAME]
