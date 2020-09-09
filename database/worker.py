from bson.objectid import ObjectId

import pymongo

client = pymongo.MongoClient("mongodb+srv://user:userpassword@cluster0.u7lzz.mongodb.net/test?retryWrites=true&w=majority")

db = client.test
collection = db.posts


def get_post_by_id(id: str):
    result = collection.find_one({'_id': ObjectId(id)})
    result['id'] = str(result.pop('_id'))
    return result


def get_posts():
    raw_result = list(collection.find({}))
    result = []
    for entry in raw_result:
        entry['id'] = str(entry.pop('_id'))
        result.append(entry)
    return result


def insert_post(post: dict):
    return str(collection.insert_one(post).inserted_id)

