#!/usr/bin/env python3
""" 102-log_stats module"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ Improves 12-log_stats.py by adding the top 10
    of the most present IPs in the collection nginx
    of the database logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    logs = collection.count_documents({})
    print('{} logs'.format(logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = collection.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, count))

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print('{} status check'.format(status_check))

    top_ips = collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print('\t{}: {}'.format(ip, count))
