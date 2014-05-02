# -*- coding: utf-8 -*-
'''
Store data on btrfs
'''

from os import makedirs, rename
from os.path import exists, join
from json import loads, dumps

def get_dataset(location, name):
    '''
    Read all data for a dataset
    >>> get_dataset('/home/deniskuzin/tivar', 'testdataset')
    []
    '''
    path = join(location, '%s.json' % name)
    if exists(path):
        with open(path, 'r') as file:
            return loads(file.read())

def set_dataset(location, name, data):
    '''
    Atomic write all data for a dataset
    >>> set_dataset('/home/deniskuzin/tivar', 'testdataset', [])
    '''
    if not exists(location):
        makedirs(location)
    path = join(location, '%s.json' % name)
    log = join('%s.log' % path)
    with open(log, 'w') as file:
        file.write(dumps(data))
    rename(log, path)

if __name__ == "__main__":
    import doctest
    doctest.testmod()