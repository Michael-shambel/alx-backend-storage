#!/usr/bin/env python3
"""
function that inserts
 the new document in the collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    collection and data provided and the id or the 
    new object will be return
    """
    result = mongo_collection.insert(kwargs)
    return result.inserted_id