#!/usr/bin/env python3
"""
python script that provides some stats about Nginx logs stored in mongoDb
"""
from pymongo import MongoClient


def logs(mongo_collection):
    """
    this function accept mongo collection and return collections
    """
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_count = {mongo_collection.count_documets({"method": method}) for method in methods}
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{total_logs} logs")
    print("Methods:")
    for metd in methods:
        print(f"method {metd}: {methods_count[metd]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient()
    nginx_collection = client.logs.nginx
    logs(nginx_collection)