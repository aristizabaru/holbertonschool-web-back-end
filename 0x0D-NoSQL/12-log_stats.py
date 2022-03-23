#!/usr/bin/env python3
""" 12-log_stats module
"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ Python script that provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    n_logs = collection.count_documents({})
    print('{} logs'.format(n_logs))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, count))

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print('{} status check'.format(status_check))
