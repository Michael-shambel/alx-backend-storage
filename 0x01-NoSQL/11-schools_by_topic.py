#!/usr/bin/env python3
"""
function that return
the list of school having the specifc topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    the function that accept mongo collection and topic and return
    the name school that have the specific topics
    """
    schoolList = mongo_collection.find({"topics": topic})
    return list(schoolList)
