#!/usr/bin/env python3
'''Task 14.
'''


def top_students(mongo_collection):
    '''To print all students in a collection sorted by average score.
    '''
    studnts = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return studnts
