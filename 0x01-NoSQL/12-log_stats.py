#!/usr/bin/env python3
'''Task 12.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''To print states about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for mtd in methods:
        req_cnt = len(list(nginx_collection.find({'method': mtd})))
        print('\tmethod {}: {}'.format(mtd, req_cnt))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
