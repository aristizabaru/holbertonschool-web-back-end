#!/usr/bin/env python3
""" 11-schools_by_topic modile
"""


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic
    """
    documents = mongo_collection.find({"topics": topic})
    documents_list = [doc for doc in documents]
    return documents_list
