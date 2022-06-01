from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps, loads
from bson import ObjectId

from core.db import get_collection


@csrf_exempt
def todos(request, item_id=None):
    if request.method == 'GET':
        return HttpResponse(get_all_todos())

    elif request.method == 'POST':
        write(loads(request.body))
        return HttpResponse(status=200)

    elif request.method == 'PUT':
        if not item_id:
            raise Http404
        update(loads(request.body))
        return HttpResponse(status=200)

    elif request.method == 'DELETE':
        delete(ObjectId(item_id))
        return HttpResponse(status=200)


def get_all_todos():
    collection = get_collection()
    res = [doc for doc in collection.find()]
    if res:
        for doc in res:
            doc['_id'] = str(doc['_id'])
    return dumps(res)


def write(record: dict):
    """
    Write a new record to the db.

    Args:
        record (dict): record to write to database.
    """
    collection = get_collection()
    # record['_id'] = ObjectId(record['_id'])
    collection.insert_one(record)


def update(data):
    id = ObjectId(data.pop('_id'))
    collection = get_collection()
    collection.update_one({'_id': id}, {'$set': data})


def delete(id):
    collection = get_collection()
    collection.delete_one({'_id': id})
