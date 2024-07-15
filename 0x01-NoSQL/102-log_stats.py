#!/usr/bin/env python3
'''Task 15.
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


def print_top_ips(server_collection):
    '''To print statistics about top 10 HTTP IPs in a collection.
    '''
    print('IPs:')
    request_logs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for rqst_log in request_logs:
        ip = rqst_log['_id']
        ip_requests_count = rqst_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))


def run():
    '''To provide some statzs about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)
    print_top_ips(client.logs.nginx)


if __name__ == '__main__':
    run()
