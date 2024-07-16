#!/usr/bin/env python3
"""
function that list all documents in a collection
"""


def list_all(mongo_collection):
    """
    return the list of all document in a collections 
    """
    documents = list(mongo_collection.find())
    return documents
