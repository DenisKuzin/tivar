# -*- coding: utf-8 -*-
'''
Store data on btrfs
'''

from settings import settings
from os import mkdir, makedirs
from os.path import exists, join
from json import loads, dumps

def init(source_name, source_schema):
    '''
    Create empty
    '''
    base_path = settings['storage']['btrfsdb']['base_path']
    if not exists(base_path):
        makedirs(base_path)
    index_path = join(base_path, 'index.json')
    if exists(index_path):
        index_file = open(index_path, 'r+')
        index = loads(index_file.read())
    else:
        index_file = open(index_path, 'w')
        index = {}
    index[source_name] = {}
    index_file.write(dumps(index))
    mkdir(join(base_path, source_name))