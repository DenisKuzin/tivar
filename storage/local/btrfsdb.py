# -*- coding: utf-8 -*-
'''
Store data on btrfs
'''

from os import makedirs, rename
from os.path import exists, join
from yaml import load, dump

location = '/home/deniskuzin/btrfsdb'

def get_dataset(name):
    '''
    Read all data for a dataset
    >>> get_dataset('testdataset')
    []
    '''
    path = join(location, '%s.yaml' % name)
    if exists(path):
        with open(path, 'r') as file:
            return load(file.read())

def set_dataset(name, data):
    '''
    Atomic write all data for a dataset
    >>> set_dataset('testdataset', [])
    '''
    if not exists(location):
        makedirs(location)
    path = join(location, '%s.yaml' % name)
    log = join('%s.log' % path)
    with open(log, 'w') as file:
        file.write(dump(data))
    rename(log, path)

if __name__ == "__main__":
    import doctest
    doctest.testmod()