# -*- coding: utf-8 -*-
u'''
Общие для всех модулей штуки
'''
from os.path import exists, isdir
from os import remove, makedirs

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