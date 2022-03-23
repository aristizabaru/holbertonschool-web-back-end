#!/usr/bin/env python3
""" 8-all module """


def list_all(mongo_collection):
    """lists all documents in a collection
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
