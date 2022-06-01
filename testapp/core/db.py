from typing import Collection
from pymongo.mongo_client import MongoClient
from django.conf import settings

# TODO: consider moving staff to settings/envs
DB_NAME = 'testapp'
TEST_COLLECTION_NAME = 'testcollection'


def get_collection(db_name=None, host=None, port=None, username=None, password=None, collection=None):

    client = MongoClient(
        host=host,
        port=int(port) if port else None,
        username=username,
        password=password
    )

    db_handle = client[db_name or DB_NAME]
    return db_handle[collection or TEST_COLLECTION_NAME]
