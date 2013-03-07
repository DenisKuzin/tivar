#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import check_dir
from settings import data_dir
from retrieve import forts

if __name__ == '__main__':
    check_dir(data_dir)
    forts.download_files()