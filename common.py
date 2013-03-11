# -*- coding: utf-8 -*-
u'''
Общие для всех модулей штуки
'''
from os.path import exists, isdir, join
from os import remove, makedirs, rename
from settings import data_dir
from requests import get

def check_dir(path):
    u'''
    Проверяет, чтобы папочка существовала, если её нет - создаёт
    Если с таким именем лежит файлик - удаляет, и создаёт папочку
    '''
    if exists(path):
        if not isdir(path):
            remove(path)
            makedirs(path)
    else:
        makedirs(path)

def download_file(file_type, direct_link):
    check_dir(join(data_dir, file_type))
    file_path = join(data_dir, file_type, direct_link.split('/')[-1])
    if not exists(file_path):
        with open(u'%s.tmp' % file_path, 'wb') as current_file:
            current_file.write(get(direct_link).content)
        rename(u'%s.tmo', file_path)