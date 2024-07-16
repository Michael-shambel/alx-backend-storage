#!/usr/bin/env python3
"""
functiion that changes all the topics of a school document on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    function that accept pymongo colllection and the name of the collection
    and update the topic given to the collection
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )