#!/usr/bin/env python3
""" 101-students module
"""


def top_students(mongo_collection):
    """ returns all students sorted by average score
    """
    students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return students
