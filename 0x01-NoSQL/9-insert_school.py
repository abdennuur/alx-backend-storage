#!/usr/bin/env python3
'''Task 9.
'''


def insert_school(mongo_collection, **kwargs):
    '''to insert new doc in a collection.
    '''
    rslt = mongo_collection.insert_one(kwargs)
    return rslt.inserted_id
